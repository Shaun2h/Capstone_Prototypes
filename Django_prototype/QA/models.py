from django.db import models
# Create your models here.
from django.contrib import admin
allowed = ["Amazon", "Apple", "Hp", "Samsung", "Intel"]


class BaseClass(models.Model):
    # City ID records which city is it.. based off the choice above.
    region = models.CharField(max_length=50, choices=(('NA', 'NA'),
                                                      ('SEA', 'SEA'),
                                                      ('EUR', 'Europe'),
                                                      ('ASIA', 'ASIA'),
                                                      ('CHINA', 'CHINA')))
    city_ID = models.IntegerField()
    product_ID = models.CharField(max_length=50, default="")
    target = models.CharField(max_length=300, default="")


    def getEQ(self):
        return "NULL"

    def __str__(self):
        return self.getEQ() + "  Region: " + str(self.region) + "  CityID: "+str(self.city_ID) \
           + " Product ID:" + str(self.product_ID) + " target url: " + str(self.target)


admin.site.register(BaseClass)


class Amazon(models.Model):
    company = models.CharField(max_length=50, default="Amazon")
    information = models.OneToOneField(BaseClass, on_delete=models.CASCADE, primary_key=True)

    def getEQ(self):
        return "Amazon"


admin.site.register(Amazon)


class Intel(models.Model):
    company = models.CharField(max_length=50, default="Intel")
    information = models.OneToOneField(BaseClass, on_delete=models.CASCADE, primary_key=True)

    def getEQ(self):
        return "Intel"


admin.site.register(Intel)


class Apple(models.Model):
    company = models.CharField(max_length=50, default="Apple")
    information = models.OneToOneField(BaseClass, on_delete=models.CASCADE, primary_key=True)

    def getEQ(self):
        return "Apple"


admin.site.register(Apple)


class Hp(models.Model):
    company = models.CharField(max_length=50, default="Hp")
    information = models.OneToOneField(BaseClass, on_delete=models.CASCADE, primary_key=True)

    def getEQ(self):
        return "Hp"


admin.site.register(Hp)


class Samsung(models.Model):
    company = models.CharField(max_length=50, default="Samsung")
    information = models.OneToOneField(BaseClass, on_delete=models.CASCADE, primary_key=True)

    def getEQ(self):
        return "Samsung"


admin.site.register(Samsung)

