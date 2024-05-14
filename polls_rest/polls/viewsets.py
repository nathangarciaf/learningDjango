from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from polls.serializers import QuestionSerializer, ChoiceSerializer
from polls.models import Question, Choice

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by('pub_date')
    serializer_class = QuestionSerializer

    @action(detail=True, methods=['get'])
    def choices(self, request, pk=None):
        question = self.get_object()
        choices = question.choice_set.all()
        serializer = ChoiceSerializer(choices, many=True, context={'request': request})
        return Response(serializer.data)

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all().order_by('votes')
    serializer_class = ChoiceSerializer
 
    @action(detail=True, methods=['post'])
    def vote(self, request, pk=None):
        choice = self.get_object()
        try:
            choice.votes += 1
            choice.save()
            return Response({"message": "Vote recorded."})
        except:
            return Response({"error": "Failed to record vote."}, status=400)