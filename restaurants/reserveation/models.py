from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class reservation(models.Model):
    name = models.CharField(_("نام و نام خانوادگی"), max_length=200)
    student_number = models.CharField(_("شماره ی دانشجویی"), max_length=200)
    phone = models.CharField(_("تلفن "), max_length=200)
    Food_name = models.CharField(_("نام غذا"), max_length=100)
    number = models.IntegerField(_("تعداد"))
    date = models.DateField(_("تاریخ"), auto_now=False, auto_now_add=False)
    time = models.TimeField(_("ساعت"), auto_now=False, auto_now_add=False)

    def __str__(self):
       return self.phone
    