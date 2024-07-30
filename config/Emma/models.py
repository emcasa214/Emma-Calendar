from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # Lưu ý: Nên sử dụng hàm mã hóa
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    priority = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    list = models.ForeignKey('List', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class List(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    color = models.CharField(max_length=7, default="#FFFFFF")  # Hex color code

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tasks = models.ManyToManyField(Task)

    def __str__(self):
        return self.name
    
class Reminder(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    remind_at = models.DateTimeField()
    repeat = models.CharField(max_length=50, blank=True)  # e.g. "daily", "weekly", "monthly"

    def __str__(self):
        return f"Reminder for {self.task.title}"
