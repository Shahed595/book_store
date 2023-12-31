from django.urls import path
# from book.views import home,store_book,show_books,edit_book,delete_book
from . import views

urlpatterns = [
    # path('', home, name="home"),
    # path('', views.TemplateView.as_view(template_name='home.html')),
    path('<int:rool>/', views.MyTemplateView.as_view(), {'author':'rahim'}, name='homepage'),
    path('store_new_book/', views.store_book, name="storeBook"),
    # path('show_books/', views.show_books, name="show_books"),
    path('show_books/', views.BookListView.as_view(), name="show_books"),
    path('edit_book/<int:id>', views.edit_book, name="edit_book"),
    path('delete_book/<int:id>', views.delete_book, name="delete_book"),
]
