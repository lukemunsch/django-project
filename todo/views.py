"""this page is to create renders of our web pages"""
from django.shortcuts import render
from .models import Item


# Create your views here.
def get_todo_list(request):
    """processing our todo list render for viewing a webpage"""
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    """processing our add item to render a view"""
    return render(request, 'todo/add_item.html')
