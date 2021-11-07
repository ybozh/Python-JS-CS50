from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")


def index(request):

    # Перевіряємо, чи ключ «завдання» вже існує у нашій сесії

    if "tasks" not in request.session:

        # Якщо ні, створюємо новий список
        request.session["tasks"] = []

    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })


def add(request):
    if request.method == "POST":

        # Отримуємо дані, відправлені користувачем, і зберігаємо їх у вигляді форми
        form = NewTaskForm(request.POST)

        # Перевіряємо, чи дані форми дійсні (зі сторони сервера) 
        if form.is_valid():

            # Відділяємо завдання від «очищеної» версії даних форми
            task = form.cleaned_data["task"]

            # Додаємо нове завдання до нашого списку завдань
            request.session["tasks"] += [task]

            # Перенаправлюємо користувача до списку завдань
            return HttpResponseRedirect(reverse("tasks:index"))
        else:

            # Якщо форма недійсна, повторно візуалізуємо сторінку з наявною інформацією.
            return render(request, "tasks/add.html", {
                "form": form
            })

    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })

