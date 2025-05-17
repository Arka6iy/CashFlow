from django.db import models


class Status(models.Model):
    name = models.CharField(blank=True,max_length=50)
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(blank=True, max_length=50)
    def __str__(self):
        return self.name

class Kind(models.Model):
    name = models.CharField(blank=True, max_length=50)
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Combo(models.Model):
    kind  = models.ForeignKey(Kind, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.kind} - {self.category} - {self.sub_category}"

class Transaction(models.Model):
    created_at = models.DateTimeField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE, blank=True, null=True)
    combo = models.ForeignKey(Combo,on_delete=models.CASCADE)
    amount = models.FloatField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)

