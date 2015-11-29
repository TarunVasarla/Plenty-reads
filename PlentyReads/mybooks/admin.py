from django.contrib import admin

 # bookid = models.IntegerField(default=0)
 #    bookname = models.CharField(max_length=200)
 #    preface = models.CharField(max_length=4000)
 #    AuthorName = models.CharField(max_length=200)
 #    AvailableYN = models.CharField(max_length=1)
 #    create_date = models.DateTimeField('create date')
 #    update_date = models.DateTimeField('update date')
 #    genre = models.IntegerField(default=0)

# Register your models here.
from .models import Book, User,genreType,wishlist,ReadHistory
# class ChoiceInline(admin.TabularInline):
#     model = Choice
#     extra = 3

class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['bookname']}),
        ('Author Name', {'fields': ['AuthorName'],'classes': ['collapse']}),
        # ('AvailableYN', {'fields': ['AvailableYN'],'classes': ['collapse']}),
        ('preface',{'fields': ['preface'],'classes':['collapse']}),
        ('genre',{'fields': ['genre'],'classes':['collapse']}),
        ('upload Book',{'fields': ['uploadBook'],'classes':['collapse']}),
        # ('create_date',{'fields': ['create_date'],'classes':['collapse']}),
        # ('update_date',{'fields': ['update_date'],'classes':['collapse']}),
    ]
    list_display = ('bookname', 'AuthorName', 'preface','genre','uploadBook','AvailableYN','create_date','update_date')
    # list_filter = ['create_date']
    search_fields = ['bookname']
    # inlines = [ChoiceInline]




class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('email', {'fields': ['email'],'classes': ['collapse']}),
        ('password', {'fields': ['password'],'classes': ['collapse']}),
        # ('ActiveYN',{'fields': ['ActiveYN'],'classes':['collapse']}),
        # ('create_date',{'fields': ['create_date'],'classes':['collapse']}),
    ]
    list_display = ('name', 'email', 'password','ActiveYN','create_date')
    search_fields = ['name']

class genreTypeAdmin(admin.ModelAdmin):
    fieldsets = [
        # (None,               {'fields': ['id']}),
        ('type', {'fields': ['type'],'classes': ['collapse']}),
    ]
    # list_display = ('type')
    search_fields = ['type']

class ReadHistoryAdmin(admin.ModelAdmin):
    fieldsets = [
        # (None,               {'fields': ['userid']}),
        ('userid', {'fields': ['userid'],'classes': ['collapse']}),
        ('bookid', {'fields': ['bookid'],'classes': ['collapse']}),
        # ('create_date',{'fields': ['create_date'],'classes':['collapse']}),
    ]
    list_display = ('userid', 'bookid','create_date')
    search_fields = ['userid']

class wishlistAdmin(admin.ModelAdmin):
    fieldsets = [
        # (None,               {'fields': ['id']}),
        ('userid', {'fields': ['userid'],'classes': ['collapse']}),
        ('bookid', {'fields': ['bookid'],'classes': ['collapse']}),
        # ('deletedYN', {'fields': ['deletedYN'],'classes': ['collapse']}),
        # ('create_date',{'fields': ['create_date'],'classes':['collapse']}),
        # ('update_date',{'fields': ['update_date'],'classes':['collapse']}),
    ]
    list_display = ('userid', 'bookid','deletedYN','create_date','update_date')
    search_fields = ['userid']



admin.site.register(genreType, genreTypeAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(wishlist, wishlistAdmin)
admin.site.register(ReadHistory, ReadHistoryAdmin)
# admin.site.register(Choice)