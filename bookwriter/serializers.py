from rest_framework import serializers
from . models import *
from rest_framework import status
from rest_framework.exceptions import ValidationError


class SectionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Section
		fields = '__all__'


class GetSectionSerializer(serializers.ModelSerializer):
	parent_section = SectionSerializer()
	child_sections = serializers.SerializerMethodField()

	class Meta:
		model = Section
		fields = '__all__'


	def get_child_sections(self, obj):
		sections = Section.objects.filter(parent_section = obj)
		return GetSectionSerializer(sections, many=True).data
