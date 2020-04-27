from django.db import models

# Create your models here.

class exams(models.Model):
	pm_type = models.CharField(max_length=250, default=0, choices=(('FLC', 'FLC'), ('FSC', 'FSC'),
																   ('Crate', 'Crate'), ('other', 'Other')))
	outer_length = models.IntegerField(default=0, blank=True, null=True)
	outer_breadth = models.IntegerField(default=0, blank=True, null=True)
	outer_height = models.IntegerField(default=0, blank=True, null=True)
	inner_length = models.IntegerField(default=0, blank=True, null=True)
	inner_breadth = models.IntegerField(default=0, blank=True, null=True)
	inner_height = models.IntegerField(default=0, blank=True, null=True)
	type_of_inserts = models.IntegerField(default=0, blank=True, null=True)

	sep_sheet_perpm = models.IntegerField(default=0, blank=True, null=True)
	ss_length = models.IntegerField(default=0, blank=True, null=True)
	ss_breadth = models.IntegerField(default=0, blank=True, null=True)
	ss_height = models.IntegerField(default=0, blank=True, null=True)
	ss_type = models.IntegerField(default=0, blank=True, null=True)
	ss_weight = models.IntegerField(default=0, blank=True, null=True)
	ss_thickness = models.IntegerField(default=0, blank=True, null=True)
	ss_gsm = models.IntegerField(default=0, blank=True, null=True)
	total_pm_permonth = models.IntegerField(default=0, blank=True, null=True)
	total_weight_capacity = models.IntegerField(default=0, blank=True, null=True)
	remarks = models.CharField(max_length=250, default=0, blank=True, null=True)
	created_on = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.created_on

class SubExam(models.Model):
	parent_exam = models.IntegerField(default = None)
	no_of_inserts_perit = models.IntegerField(default=0, blank=True, null=True)

	insert_length = models.IntegerField(default=0, blank=True, null=True)
	insert_breadth = models.IntegerField(default=0, blank=True, null=True)
	insert_height = models.IntegerField(default=0, blank=True, null=True)

	insert_type = models.IntegerField(default=0, blank=True, null=True)
	insert_weight = models.IntegerField(default=0, blank=True, null=True)
	insert_thickness = models.IntegerField(default=0, blank=True, null=True)
	insert_gsm = models.IntegerField(default=0, blank=True, null=True)
	parts_per_layer = models.IntegerField(default=0, blank=True, null=True)
	pocket_length = models.IntegerField(default=0, blank=True, null=True)
	pocket_breadth = models.IntegerField(default=0, blank=True, null=True)
	pocket_height = models.IntegerField(default=0, blank=True, null=True)
	matrix_detail = models.CharField(max_length=250, default=0, blank=True, null=True)

	def __str__(self):
		return self.parent_exam