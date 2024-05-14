from rest_framework import serializers
from polls.models import Poll

from django.contrib.auth.models import User

class PollSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='poll-highlight', format='html')

    class Meta:
        model = Poll
        fields = ['url', 'id', 'highlight', 'owner'
                  'question_text', 'pub_date']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    polls = serializers.HyperlinkedRelatedField(many=True, view_name='poll-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'poll']