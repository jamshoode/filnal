from students.models import Students, MarkAndPresence
from .serializers import StudentSerializer, MarkAndPresenceSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics


class StudentViewSet(viewsets.ModelViewSet):
	queryset = Students.objects.all()
	serializer_class = StudentSerializer
	
	def list(self, request):
		query = self.queryset
		print(request.GET.get('date'))
		if request.GET.get('date'):
			query = MarkAndPresence.objects.filter(date=request.GET.get('date'))
			serialize = MarkAndPresenceSerializer(query, many=True)
		else:
			serialize = StudentSerializer(query, many=True)

		if request.GET.get('presence'):
			query = query.filter(presence=request.GET.get('presence'))
			serialize = MarkAndPresenceSerializer(query, many=True)
		return Response(serialize.data)


class StudentMarkPresenceViewSet(viewsets.ModelViewSet):
	queryset = MarkAndPresence.objects.all()
	serializer_class = MarkAndPresenceSerializer
