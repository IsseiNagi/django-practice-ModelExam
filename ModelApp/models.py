from django.db import models

# Create your models here.


class Classes(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'classes'


class Students(models.Model):
    class_name = models.ForeignKey(Classes, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    grade = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'students'


class Tests(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tests'


class TestResults(models.Model):
    score = models.IntegerField()
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    test = models.ForeignKey(Tests, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'test_results'

