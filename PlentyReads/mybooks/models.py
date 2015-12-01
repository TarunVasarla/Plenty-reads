import datetime
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import BaseUserManager

from pdfminer.converter import HTMLConverter
from pdfminer.pdfinterp import PDFResourceManager, process_pdf

from pdfminer.layout import LAParams
import hashlib
import urllib
import sys
import os

from django.conf import settings 
# from pdfminer.pdfpage import PDFPage


import sys
reload(sys)
sys.setdefaultencoding("utf-8")


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
  name = models.CharField(max_length=50)
  email = models.CharField(max_length=100,unique=True)
  password = models.CharField(max_length=30)
  ActiveYN  = models.CharField(max_length=1,default='Y')
  create_date = models.DateTimeField(default=datetime.datetime.now())

  # objects = MyUserManager()
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



class Pdf(models.Model):
        id=models.CharField(max_length=32,primary_key=True)
        url=models.URLField()
        
        @staticmethod
        def fromUrl(url):
            try:
                pdf=Pdf.objects.get(id=Pdf.__getId(url))
            except Pdf.DoesNotExist:
                pdf=Pdf()
                pdf.id=None
                pdf.url=url
                
            return pdf
        
        def getPath(self):
            return urllib.urlretrieve(self.url)[0]
        
        def __eq__(self, pdf):
            return self.id==pdf.id
        
        def save(self):
            if self.id==None:
                self.id=self.__getId(self.url)
            super(Pdf,self).save()
        
        @staticmethod
        def __getId(url):
            return hashlib.md5(url).hexdigest()
        
class Html(models.Model):
    pdf=models.ForeignKey("Pdf")
    content=models.TextField()
        
    def write(self, text):
        self.content += text
        
    def toString(self):
        return self.content

class   PdfManager():
    pdf=None
    caching=True
    codec = 'utf-8'
    scale=1
    layoutmode = 'normal'
    laparams = LAParams()
    outdir = None
    pagenos=set()
    maxpages=0
    password=''
    
    def __init__(self,pdf):
        self.__pdf=pdf
        
    def outToHtml(self, html):
        # pdf   File=file('C:/Python27/Scripts/PlentyReads/mybooks/uploads/4ABSLIST_OF_FIGABBREVATIONS.pdf', 'rb')
        # self.__pdf.getPath()
        # # path = settings.MEDIA_URL+Pdf.objects.get(id=Pdf.__getId(self.))
        # pdfFile=file(path ,'rb')
    

        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        MEDIA_ROOT = os.path.join(BASE_DIR,'mybooks\\')

        pdfFile=file(MEDIA_ROOT + str(self.__pdf.url), 'rb')
        rsrcmgr = PDFResourceManager(caching=self.caching)
        device = HTMLConverter(rsrcmgr, html, codec=self.codec, 
                               scale=self.scale,layoutmode=self.layoutmode, 
                               # laparams=self.laparams, outdir=self.outdir)
                               laparams=self.laparams)
        process_pdf(rsrcmgr, device, pdfFile, self.pagenos, maxpages=self.maxpages, password=self.password,
                          caching=self.caching, check_extractable=True)
        # PDFPage.get_pages(fp=pdfFile, maxpages=self.maxpages, 
        #                   pagenos=self.pagenos, password=self.password, caching=self.caching, 
        #                   check_extractable=True)
        pdfFile.close()
        # html.pdf=self.pdf
        
        return html

