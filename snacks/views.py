from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Snacks
from .serializers import SnacksSerializer
from .permissions import IsAuthorOrReadOnly

class SnacksList(ListCreateAPIView):
    queryset = Snacks.objects.all()
    serializer_class = SnacksSerializer

class SnacksDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly) 
    queryset = Snacks.objects.all()
    serializer_class = SnacksSerializer