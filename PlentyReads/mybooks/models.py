import datetime
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.files.storage import FileSystemStorage

class genreType(models.Model):
  id = models.AutoField(primary_key=True)
  type = models.CharField(max_length=200)

  def __unicode__(self):
    return self.type

class Book(models.Model):
  id = models.AutoField(primary_key=True)
  bookname = models.CharField(max_length=200)
  preface = models.CharField(max_length=4000)
  AuthorName = models.CharField(max_length=200)
  AvailableYN = models.CharField(max_length=1,default='Y')
  create_date = models.DateTimeField(default=datetime.datetime.now())
  update_date = models.DateTimeField(default=datetime.datetime.now())
  genre = models.ForeignKey(genreType)
  uploadBook = models.FileField(upload_to='uploads/')

  def __unicode__(self):
  	return self.bookname

class User(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=200)
  email = models.CharField(max_length=4000)
  password = models.CharField(max_length=200)
  ActiveYN  = models.CharField(max_length=1,default='Y')
  create_date = models.DateTimeField(default=datetime.datetime.now())

  def __unicode__(self):
    return self.name  


class ReadHistory(models.Model):
  id = models.AutoField(primary_key=True)
  userid = models.ForeignKey(User)
  bookid = models.ForeignKey(Book)
  create_date = models.DateTimeField(default=datetime.datetime.now())

  def __unicode__(self):
    return str(self.userid)

class wishlist(models.Model):
  id = models.AutoField(primary_key=True)
  userid = models.ForeignKey(User)
  bookid = models.ForeignKey(Book)
  deletedYN  = models.CharField(max_length=1,default='N')
  create_date = models.DateTimeField(default=datetime.datetime.now())
  update_date = models.DateTimeField(default=datetime.datetime.now())

  def __unicode__(self):
    return str(self.userid)



    # def was_published_recently(self):
    #     now = timezone.now()
    #     return now - datetime.timedelta(days=1) <= self.pub_date <= now
    #     was_published_recently.admin_order_field = 'pub_date'
    # 	was_published_recently.boolean = True
    # 	was_published_recently.short_description = 'Published recently?'
# class Choice(models.Model):
#     question = models.ForeignKey(Question)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#     def __unicode__(self): 
#     	return self.choice_text