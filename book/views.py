from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from book.forms import BookStorForm
from book.models import BookstoreModel
from django.views.generic import TemplateView, ListView

# Create your views here.
#function based view
# def home(request):
#     return render(request,"home.html")

#class based view
class MyTemplateView(TemplateView):
    template_name='home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {'name':'rahim', 'age':21}
        print(context)
        # dictionary update kora
        context.update(kwargs) 
        print(context)
        return context
    

def store_book(request):
    if request.method == 'POST':
        book = BookStorForm(request.POST)
        if book.is_valid():
            book.save()
            print(book.cleaned_data)
            return redirect('show_books')
            
    else:
        book = BookStorForm()
    return render(request,"store_book.html", {'form': book})


# Template Based View
# def show_books(request):
#     book = BookstoreModel.objects.all()
#     # print(book)
#     return render(request, 'show_book.html', {'data':book})


# Class Based View
class BookListView(ListView):
    model = BookstoreModel
    template_name= 'show_book.html'
    context_object_name = 'book_list'
    # Sorting on id or name
    # def get_queryset(self):
    #     return BookstoreModel.objects.filter(author_name = 'Shahed')
    #     return BookstoreModel.objects.filter(ID = '1')
     
    # lexiographical oeder
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context = {'Rahim' : BookstoreModel.objects.all().order_by('author_name')}
    #     return context
    # ordering = ['category']
    
    #ASC to DESC
    # ordering = ['ID'] 
    
    # DESC to ASC
    # ordering = ['-ID'] 
    
    

def edit_book(request, id):
    book = BookstoreModel.objects.get(pk=id)
    form = BookStorForm(instance=book)
    if request.method=='POST':
        book = BookStorForm(request.POST, instance=book)
        if book.is_valid():
            book.save()
            return redirect('show_books')
    return render(request, 'store_book.html', {'form': form})

def delete_book(request,id):
    book = BookstoreModel.objects.get(pk=id).delete()
    return redirect('show_books')
