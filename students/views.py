from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from .models import Students, MarkAndPresence
from students.api.serializers import StudentSerializer, MarkAndPresenceSerializer
from rest_framework import generics
