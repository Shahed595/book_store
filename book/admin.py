from django.contrib import admin
from book.models import BookstoreModel

# Register your models here.

class BookStoreModelAdmin(admin.ModelAdmin):
    list_display=('ID', 'book_name', 'author_name', 'category', 'first_pub', 'last_pub')

admin.site.register(BookstoreModel,BookStoreModelAdmin)
