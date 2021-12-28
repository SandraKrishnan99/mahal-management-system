from django.db import models

class user_register_table(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.EmailField(max_length=100)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.name
class birth_register_table(models.Model):
    childname=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    birthdate=models.DateField()
    birthplace=models.CharField(max_length=100)
    mothername=models.CharField(max_length=100)
    fathername=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    pmc=models.CharField(max_length=100)
    def __str__(self):
        return self.childname


class death_register_table(models.Model):
    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    deathdate=models.DateField()
    deathplace=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    pmc=models.CharField(max_length=100)
    def __str__(self):
        return self.name
# Create your models here.
class marriage_register_table(models.Model):
    husbandname=models.CharField(max_length=100)
    hdob=models.DateField()
    hage=models.CharField(max_length=100)
    wifename=models.CharField(max_length=100)
    wdob=models.DateField()
    wage=models.CharField(max_length=100)
    marriagedate=models.DateField()
    marriageplace=models.CharField(max_length=100)

    def __str__(self):
        return self.husbandname
class divorce_register_table(models.Model):
    husbandname=models.CharField(max_length=100)
    hage=models.CharField(max_length=100)
    wifename=models.CharField(max_length=100)
    wage=models.CharField(max_length=100)
    marriagedate=models.DateField()
    reason=models.CharField(max_length=100)

    def __str__(self):
        return self.husbandname
class madrasa_register_table(models.Model):
    childname=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    classs=models.CharField(max_length=100)
    birthdate=models.DateField()
    parentname=models.CharField(max_length=100)
    address=models.CharField(max_length=100)

    def __str__(self):
        return self.childname

class family_register_table(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    pmc=models.CharField(max_length=100)
    totalmembers=models.CharField(max_length=100)


    def __str__(self):
        return self.name

class accounts_table(models.Model):
    panchayat=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    invoice=models.CharField(max_length=100)
    billamount=models.CharField(max_length=100)
    billdate=models.CharField(max_length=100)

    def __str__(self):
        return self.panchayat

