from django.shortcuts import render,redirect
from .models import Book
from .forms import BookForm
# Create your views here.

def homepage(request):
    # 1. fetch all data of book from database
    # 2. send all fetch data to a template 
    books = Book.objects.all()
    print (books)
    
    return render(request,'book_list.html',{'books':books})

def add_book(request):
    if request.method == 'POST': 
        # when click on save button get all data from frontend
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = BookForm()
        return render(request,'add_book.html',{'form':form})
    
def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if book:
        book.delete()
        return redirect('homepage')
    
def update_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = BookForm(instance=book)
        return render(request,'add_book.html',{'form':form})
    