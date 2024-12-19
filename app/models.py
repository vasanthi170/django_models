from django.db import models

# Create your models here.

class Topic(models.Model): #models module, Model class
    topic_name = models.CharField(max_length=200,primary_key=True)

class Webpage(models.Model):
    topic_name = models.ForeignKey(Topic,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.URLField()

class AccessRecords(models.Model):
    name = models.ForeignKey(Webpage,on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    date = models.DateField()

# after creating models register them using (admin.site.register) in admin.py file.
# then migrate them using ... 
# python mange.py migrate---> it checks whether the migration follows correct spellings and all
# python mange.py makemigrations ---> it will change data to database language.
# python mange.py migrate---> it will save the data into 0001_initial.py file.
# if we dont give primary key in a table django will create by itself one row named as id or pk.
# python manage.py createsuperuser by using this command we can create on account in admin. we will use this to see the tables which we created...
 
