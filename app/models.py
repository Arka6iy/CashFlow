from django.db import models


class Status(models.Model):
    name = models.CharField(blank=True,max_length=50)
    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(blank=True, max_length=50)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(blank=True, max_length=50)
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    sub_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    data = models.CharField(max_length=50)
    def __str__(self):
        return self.data


class Transaction(models.Model):
    created_at = models.DateTimeField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE, blank=True, null=True)
    kind = models.ForeignKey(Type, on_delete=models.CASCADE,blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    sub_category = models.ForeignKey(SubCategory,on_delete=models.CASCADE, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    note = models.TextField(null=True)

