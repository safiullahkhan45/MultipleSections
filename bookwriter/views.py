from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.decorators import api_view
from . serializers import SectionSerializer, GetSectionSerializer
from . models import Section

# Create your views here.
@api_view(['POST'])
def create_section(request):
	serializer = SectionSerializer(data=request.data)
	if serializer.is_valid():
		section = serializer.save()
		serializer = GetSectionSerializer(section)
		return Response({"success": True, 'response': {'Section': serializer.data}},
					status=status.HTTP_201_CREATED)
	else:
		return Response({"success": False, 'response': {'Message': serializer.errors}},
					status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_section(request):
	section = request.query_params.get('section')
	try:
		section = Section.objects.get(id=section)
		serializer = GetSectionSerializer(section)
		return Response({"success": True, 'response': {'Section': serializer.data}},
					status=status.HTTP_200_OK)
	except Exception as e:
		return Response({"success": False, 'response': {'Message': str(e)}},
					status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_all_sections(request):
	sections = Section.objects.filter(parent_section=None)
	serializer = GetSectionSerializer(sections, many=True)
	return Response({"success": True, 'response': {'Section': serializer.data}},
					status=status.HTTP_200_OK)
