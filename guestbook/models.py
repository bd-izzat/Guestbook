from django.db import models


class Message(models.Model):
    author_name = models.CharField("Автор сообщения", max_length=100)
    author_email = models.EmailField("Электронная почта", blank=True, null=True)
    message_text = models.TextField("Сообщение")
    date_posted = models.DateTimeField("Дата публикации", auto_now_add=True)

    def __str__(self):
        return self.author_name
