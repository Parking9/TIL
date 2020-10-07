from django.test import TestCase
from accounts.models import User
from .models import Todo

# Create your tests here.
class TodoTest(TestCase):
    def setUp(self):
        User.objects.create_user(username='user', password='1234')

    def test_todo_index(self):
        response=self.client.get('/todos/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/todos/')

        #User.objects.create_user(username='user', password='1234')
        self.client.login(username='user', password='1234')
        response=self.client.get('/todos/')
        self.assertTemplateUsed(response, 'todos/index.html')
    
    #GET
    def test_todo_create(self):
        self.client.login(username='user', password='1234')
        response=self.client.get('/todos/create/')
        self.assertTemplateUsed(response,'todos/form.html')
        self.assertEqual(response.status_code, 200)

    #POST
    def test_todo_create(self):
        self.client.login(username='user', password='1234')
        
        invalid_data={
            # 'content':None
        }
        response = self.client.post('/todos/create/', invalid_data)
        self.assertEqual(response.status_code, 200)
        todos=Todo.objects.all()
        self.assertEqual(len(todos),0)

        valid_data={
            'content':'test-content'
        }
        response = self.client.post('/todos/create/', valid_data)
        todos=Todo.objects.all()
        self.assertEqual(len(todos),1)