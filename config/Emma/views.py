from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import TaskForm

# Create your views here.
def index(request):
    return render(request, 'home.html')

# def create_task(request):
#     if request.method == 'POST':
#         form = TaskForm(request.POST, user=request.user)
#         if form.is_valid():
#             task = form.save(commit=False)
#             if request.user.is_authenticated:
#                 task.user = request.user
#             task.save()
#             return redirect('task_list')
#     else:
#         form = TaskForm(user=request.user)
#     return render(request, 'create_task.html', {'form': form})

def create_task(request):
    form = TaskForm()
    return render(request, 'create_task.html', {'form': form})