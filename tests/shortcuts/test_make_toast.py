from django.shortcuts import make_toast
from django.test import SimpleTestCase

class MakeToastTests(SimpleTestCase):
	#  no __init__  required? Nope, not really. Python will 
	#  add, I'm guessing, a default contructor. 


	def test_make_toast(self):
		self.assertEqual(make_toast(), 'toast')

















  