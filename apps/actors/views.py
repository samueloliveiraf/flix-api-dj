from rest_framework import generics

from apps.actors.serializers import ActorsSerializer
from apps.actors.models import Actors


class ActorCreateListView(generics.ListCreateAPIView):
    queryset = Actors.objects.all()
    serializer_class = ActorsSerializer


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actors.objects.all()
    serializer_class = ActorsSerializer


class ActorRetrieveView(generics.RetrieveAPIView):
    queryset = Actors.objects.all()
    serializer_class = ActorsSerializer
