from django.db import models
from django.core.validators import MaxValueValidator


# Create your models here.

class Student(models.Model):
    Name = models.CharField(max_length=50)
    Sure_Name = models.CharField(max_length=50)
    Age = models.PositiveIntegerField()
    Course = models.CharField(max_length=50)
    musical_instrument = (
        ("g", "Гитара"),
        ("f", "Фортепиано"),
        ("b", "Барабаны"),
        ("s", "Скрипка"),
        ("t", "Труба"),
        ("a", "Аккордеон"),
    )
    Musical_Instrument = models.CharField(max_length=50, choices=musical_instrument)
    Progress = models.PositiveIntegerField(validators=[MaxValueValidator(12)])
    payment = (
        ("true", "Заплатил"),
        ("false", "Не заплатил"),
    )
    Payment = models.CharField(max_length=50, choices=payment)

    def __str__(self):
        return f"{self.Name} - {self.Sure_Name}"

    def get_absolute_url(self):
        return f"/{self.pk}"

    def get_absolute_url_editing(self):
        return f"edit/{self.pk}"
