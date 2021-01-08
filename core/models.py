from django.db import models


class People(models.Model):
    MALE = "M"
    FEMALE = "F"
    GENDER_CHOICE = (
        (MALE, "Masculino"),
        (FEMALE, "Feminino"),
    )

    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=20, choices=GENDER_CHOICE)
    weight = models.DecimalField(decimal_places=3, max_digits=5)
    programming_lenguage = models.ForeignKey("ProgrammingLenguage", on_delete=models.PROTECT)

    class Meta:
        ordering = ['name']
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"


    def __str__(self):
        return self.name

class ProgrammingLenguage(models.Model):
    EASY = 'easy'
    MEDIUM = 'medium'
    HARD = 'hard'
    DIFFICULTY_CHOICE = (
        (EASY, "Fácil"),
        (MEDIUM, "Médio"),
        (HARD, "Difícil"),
    )
    name = models.CharField(max_length=255)
    learning_difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICE)

    class Meta:
        ordering = ['name']
        verbose_name = "Linguagem de Programação"
        verbose_name_plural = "Linguagens de Programação"

    def __str__(self):
        return self.name
