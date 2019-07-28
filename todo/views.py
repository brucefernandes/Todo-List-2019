from django.shortcuts import render
from django.http import  HttpResponseRedirect
from .models import TodoItem
from django.views.generic import ListView, CreateView



class TodoList(ListView):
	template_name = 'todo.html'
	model = TodoItem

	context_object_name = 'items'




'''
def todoView(request):
	items = TodoItem.objects.all()
	return render(request,'todo.html',
			{ 'all_items': items })
'''


class CreateTodoItem(CreateView):
	model = TodoItem
	fields = ['content']






def addTodo(request):
	new_item = TodoItem(content = request.POST['content'])
	new_item.save()
	return HttpResponseRedirect('/todo/')

	#create a new tod all_items
	#save
	#redirect the browser to '/todo/'

def deleteTodo(request, todo_id):

	item_to_delete = TodoItem.objects.get(id=todo_id)
	item_to_delete.delete()

	return HttpResponseRedirect('/todo/')
