from rest_framework import serializers
from .models import Contact


def contact_serializer_factory(type='basic'):
    if  type == 'basic':
        res_fields = 'pk first_name author'.split()
    elif type == 'full':
        res_fields = 'pk first_name last_name address city work_phone mobile_phone created_at last_modified is_private author'.split()

    class ContactSerializer(serializers.ModelSerializer):
        author = serializers.ReadOnlyField(source='author.username')

        class Meta:
                model = Contact
                fields = res_fields

    return ContactSerializer


BasicContactSerializer = contact_serializer_factory('basic')
FullContactSerializer = contact_serializer_factory('full')
