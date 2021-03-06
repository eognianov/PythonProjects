from contacts.models import Contact
from .serializers import BasicContactSerializer, FullContactSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrReadOnly, IsPrivate


# Create your views here.
class ContactsList(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = BasicContactSerializer
    permission_classes = (IsAuthenticated, )

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BasicContactSerializer
        return FullContactSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)


class ContactDetail(generics.RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = FullContactSerializer

    permission_classes = (IsPrivate, )


class ContactEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = FullContactSerializer

    permission_classes = (IsAuthorOrReadOnly, )


