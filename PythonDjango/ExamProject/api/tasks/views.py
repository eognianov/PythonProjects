from tasks.models import Task
from .serializers import BasicTaskSerializer, FullTaskSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrReadOnly, IsPrivate


class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = BasicTaskSerializer
    permission_classes = (IsAuthenticated, )

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BasicTaskSerializer
        return FullTaskSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)


class ToDoList(generics.ListAPIView):
    # TODO: Only task for logged user
    queryset = Task.objects.filter(is_finished=False, )
    serializer_class = BasicTaskSerializer

    permission_classes = (IsAuthenticated, )


class TaskDetail(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = FullTaskSerializer

    permission_classes = (IsPrivate, )


class TaskEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = FullTaskSerializer

    permission_classes = (IsAuthorOrReadOnly, )
