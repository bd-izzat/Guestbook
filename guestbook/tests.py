from django.test import TestCase, Client
from django.urls import reverse
from .models import Message


# Create your tests here.
class ChatTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_add_message_to_chat(self):
        # Создаем тестовое сообщение
        message_text = "Test message"
        author_name = "Test User"
        response = self.client.post(reverse('chat'), {'message_text': message_text, 'author_name': author_name})

        # Проверяем, что сообщение успешно добавлено
        self.assertEqual(response.status_code, 302)  # Ожидаем перенаправление после успешного добавления
        self.assertTrue(Message.objects.filter(message_text=message_text, author_name=author_name).exists())

    def test_delete_message_from_chat(self):
        # Создаем тестовое сообщение
        test_message = Message.objects.create(message_text="Test message", author_name="Test User")
        message_id = test_message.id

        # Удаляем сообщение
        response = self.client.post(reverse('delete_message', args=[message_id]))

        # Проверяем, что сообщение успешно удалено
        self.assertEqual(response.status_code, 302)  # Ожидаем перенаправление после успешного удаления
        self.assertFalse(Message.objects.filter(id=message_id).exists())
