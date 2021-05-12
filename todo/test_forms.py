from django.test import TestCase
from .forms import ItemForm

# Create your tests here. (all test names should have prefix test_)

class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        # simulate user submitting form with no name field
        form = ItemForm({'name': ''})
        # assert form is invalid
        self.assertFalse(form.is_valid())
        # invalid form provides dict of lists of errors for each field
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        # simulate user submitting form with only name field 
        form = ItemForm({'name': 'Test Todo Item'}) 
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        # instantiate an empty form
        form = ItemForm()
        # can access inner Meta class of ItemForm object
        self.assertEqual(form.Meta.fields, ['name', 'done'])