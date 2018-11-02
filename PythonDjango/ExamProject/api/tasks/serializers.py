from rest_framework import serializers
from tasks.models import Task


def task_serializer_factory(type='basic'):
    if type == 'basic':
        res_fields = 'pk name priority is_finished author'.split()
    elif type == 'full':
        res_fields = 'pk name description is_finished priority is_private created_at last_modified author'.split()

    class TaskSerializer(serializers.ModelSerializer):
        author = serializers.ReadOnlyField(source='author.username')

        class Meta:
            model = Task
            fields = res_fields

    return TaskSerializer


BasicTaskSerializer = task_serializer_factory('basic')
FullTaskSerializer = task_serializer_factory('full')
