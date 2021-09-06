
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Snacks

class SnacksModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_post = Snacks.objects.create(
            author = test_user,
            snack_name = 'snack_name of Blog',
            description = 'Words about the blog'
        )
        test_post.save()

    def test_blog_content(self):
        post = Snacks.objects.get(id=1)

        self.assertEqual(str(post.author), 'tester')
        self.assertEqual(post.snack_name, 'snack_name of Blog')
        self.assertEqual(post.description, 'Words about the blog')

class APITest(APITestCase):
    def test_list(self):
        response = self.client.get(reverse('snacks_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail(self):

        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_post = Snacks.objects.create(
            author = test_user,
            snack_name = 'snack_name of Blog',
            description = 'Words about the blog'
        )
        test_post.save()

        response = self.client.get(reverse('snacks_detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'id':1,
            'snack_name': test_post.snack_name,
            'description': test_post.description,
            'author': test_user.id,
        })


    def test_create(self):
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        url = reverse('snacks_list')
        data = {
            "snack_name":"Testing is Fun!!!",
            "description":"when the right tools are available",
            "author":test_user.id,
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED, test_user.id)

        self.assertEqual(Snacks.objects.count(), 1)
        self.assertEqual(Snacks.objects.get().snack_name, data['snack_name'])

    def test_update(self):
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_post = Snacks.objects.create(
            author = test_user,
            snack_name = 'snack_name of Blog',
            description = 'Words about the blog'
        )

        test_post.save()

        url = reverse('snacks_detail',args=[test_post.id])
        data = {
            "snack_name":"Testing is Still Fun!!!",
            "author":test_post.author.id,
            "description":test_post.description,
        }

        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK, url)

        self.assertEqual(Snacks.objects.count(), test_post.id)
        self.assertEqual(Snacks.objects.get().snack_name, data['snack_name'])


    def test_delete(self):
        """Test the api can delete a post."""

        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_post = Snacks.objects.create(
            author = test_user,
            snack_name = 'snack_name of Blog',
            description = 'Words about the blog'
        )

        test_post.save()

        post = Snacks.objects.get()

        url = reverse('snacks_detail', kwargs={'pk': post.id})


        response = self.client.delete(url)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT, url)