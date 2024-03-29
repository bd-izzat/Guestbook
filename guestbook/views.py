from django.shortcuts import render, redirect
from .forms import MessageForm  # Импортируем форму
from .models import Message


def guestbook_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('guestbook')  # Перенаправляем на страницу гостевой книги
    else:
        form = MessageForm()
    messages = Message.objects.all()
    return render(request, 'guestbook.html', {'form': form, 'messages': messages})


def chat_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chat')
    else:
        form = MessageForm()

    chat_messages = Message.objects.order_by('-date_posted')[:10]

    return render(request, 'chat.html', {'form': form, 'chat_messages': chat_messages})


def delete_message(request, message_id):
    if request.method == 'POST':
        message = Message.objects.get(pk=message_id)
        message.delete()
    return redirect('chat')  # Перенаправляем на страницу чата
