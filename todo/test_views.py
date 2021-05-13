from django.test import TestCase
from .models import Item

# Create your tests here.
class TestViews(TestCase):

    def test_get_todo_list(self):
        # use django built-in http client to send requests
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_add_item_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_edit_item_page(self):
        # create an Item instance to use for test 
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    def test_can_add_item(self):
        # send post request from built-in client
        response = self.client.post('/add', {'name': 'Test Added Item'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')  # assert that view redirects back to homepage

    def test_can_delete_item(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/delete/{item.id}')
        self.assertRedirects(response, '/')
        # filter existing item instances by item.id
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)  # should be empty if deletion was successful

    def test_can_toggle_item(self):
        item = Item.objects.create(name='Test Todo Item', done=True)
        response = self.client.get(f'/toggle/{item.id}')
        self.assertRedirects(response, '/')
        # check done field was updated
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)

    def test_can_edit_item(self):
        item = Item.objects.create(name='Test Todo Item')
        # simulate post request with updated name data
        response = self.client.post(f'/edit/{item.id}', {'name': 'Updated Name'})
        self.assertRedirects(response, '/')
        # get updated item instance by item.id
        updated_item = Item.objects.get(id=item.id)
        self.assertEqual(updated_item.name, 'Updated Name')