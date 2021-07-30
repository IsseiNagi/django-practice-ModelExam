from django.db import models

# Create your models here.


class Students(models.Model):
    class_name = models.ForeignKey('Classes', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    grade = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'students'


class Classes(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'classes'


class TestResults(models.Model):
    student = models.ForeignKey('Students', on_delete=models.CASCADE)
    test = models.ForeignKey('Tests', on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'test_results'


class Tests(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tests'

