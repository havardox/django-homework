from django.db import models


class Homework(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    due = models.DateTimeField()

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Grade(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    homework = models.OneToOneField(Homework, on_delete=models.CASCADE)
    grade = [('MA', 'MA'),
             ('2', '2'),
             ('3', '3'),
             ('4', '4'),
             ('5', '5'),
             ]
