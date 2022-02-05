from django.db import models

# Create your models here.
class Section(models.Model):
	title = models.CharField(max_length=32)
	parent_section = models.ForeignKey('Section', on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return self.title

