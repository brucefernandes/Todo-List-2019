
from django.contrib import admin
from django.urls import path
from todo.views import  addTodo, deleteTodo, TodoList

urlpatterns = [
    path('admin/', admin.site.urls),
	path('todo/', TodoList.as_view(), name='todourl'),
	


	#path('todo/', todoView),
	path('addTodo', addTodo),
	path('deleteTodo/<int:todo_id>', deleteTodo),

]
