from django.db import models

class Needy(models.Model):
    id_needy = models.AutoField(primary_key=True)  # Первинний ключ (числове поле)
    phone = models.BigIntegerField()  # Числове поле для телефону
    pib_needy = models.CharField(max_length=255)  # ПІБ працівника
    email = models.EmailField(unique=True)  # Email
    login = models.CharField(max_length=100, unique=True)  # Логін
    photo = models.CharField(max_length=255, blank=True, null=True)  # Шлях до фото
    password = models.CharField(max_length=255)  # Пароль

    def __str__(self):
        return self.pib_employee


class TypeWork(models.Model):
    code_type_work = models.AutoField(primary_key=True)  # Первинний ключ
    name = models.CharField(max_length=255)  # Назва типу роботи
    description = models.TextField()  # Опис роботи

    def __str__(self):
        return self.name

class Volunteer(models.Model):
    id_volunteer = models.AutoField(primary_key=True)  # Первинний ключ
    phone = models.BigIntegerField()  # Числове поле для телефону
    pib_volunteer = models.CharField(max_length=255)  # ПІБ волонтера
    email = models.EmailField(unique=True)  # Email
    login = models.CharField(max_length=100, unique=True)  # Логін
    photo = models.CharField(max_length=255, blank=True, null=True)  # Шлях до фото
    password = models.CharField(max_length=255)  # Пароль
    amount_of_help = models.IntegerField()  # Кількість наданої допомоги
    code_type_work = models.ForeignKey(TypeWork, on_delete=models.CASCADE)  # Зв'язок з TypeWork

    def __str__(self):
        return self.pib_volunteer
