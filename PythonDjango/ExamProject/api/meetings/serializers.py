from rest_framework import serializers
from meetings.models import Meeting


def meeting_serializer_factory(type='basic'):
    if type == 'basic':
        res_fields = 'pk name author'.split()
    elif type == 'full':
        res_fields = 'pk name place date start_at duration is_private created_at last_modified author'.split()

    class MeetingSerializer(serializers.ModelSerializer):
        author = serializers.ReadOnlyField(source='author.username')

        class Meta:
            model = Meeting
            fields = res_fields

    return MeetingSerializer


BasicMeetingSerializer = meeting_serializer_factory('basic')
FullMeetingSerializer = meeting_serializer_factory('full')
