from django.utils.datetime_safe import date

from meetings.models import Meeting
from .serializers import BasicMeetingSerializer, FullMeetingSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrReadOnly, IsPrivate


class MeetingList(generics.ListCreateAPIView):
    queryset = Meeting.objects.all()
    serializer_class = BasicMeetingSerializer
    permission_classes = (IsAuthenticated, )

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BasicMeetingSerializer
        return FullMeetingSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)


class TodayList(generics.ListAPIView):
    today_date = date.today()

    queryset = Meeting.objects.filter(date=today_date)
    serializer_class = BasicMeetingSerializer

    permission_classes = (IsAuthenticated, )


class MeetingDetail(generics.RetrieveAPIView):
    queryset = Meeting.objects.all()
    serializer_class = FullMeetingSerializer

    permission_classes = (IsPrivate, )


class MeetingEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meeting.objects.all()
    serializer_class = FullMeetingSerializer

    permission_classes = (IsAuthorOrReadOnly, )
