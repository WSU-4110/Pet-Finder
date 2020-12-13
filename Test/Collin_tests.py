from django.test import TestCase
from django.urls import reverse

from petManager.models import pets
from django.template import RequestContext
from django.template.loader import render_to_string


# Create your tests here.

class PetsTestCase(TestCase):
    def setUp(self):
        pets.objects.create(animal="TestAnimal1", breed="TestBreed1", name="TestName1",
                                   color="TestColor1")
        pets.objects.create(animal="TestAnimal2", breed="TestBreed2", name="TestName2",
                            color="TestColor2")

    def test_proper_creation(self):
        petstest1 = pets.objects.get(animal="TestAnimal1")
        self.assertEqual(petstest1.animal, 'TestAnimal1')

    def test_separate_values_pass(self):
        petstest1 = pets.objects.get(animal="TestAnimal1")
        petstest2 = pets.objects.get(animal="TestAnimal2")
        self.assertNotEqual(petstest1.animal, petstest2.animal)

    def test_separate_values_fail(self):
        petstest1 = pets.objects.get(animal="TestAnimal1")
        petstest2 = pets.objects.get(animal="TestAnimal2")
        self.assertEqual(petstest1.animal, petstest2.animal)

    def test_if_part_of_class(self):
        petstest1 = pets.objects.get(animal="TestAnimal1",breed="TestBreed1", name="TestName1",
                                   color="TestColor1")
        self.assertIsInstance(petstest1, pets)



        
        
        
    def test_isnot_instance_of_class(self):
            petstest1 = pets.objects.get(animal="TestAnimal1", breed="TestBreed1", name="TestName1",
                                         color="TestColor1")
            self.assertNotIsInstance(petstest1.animal, pets)

    def test_color(self):
        petstest1 = pets.objects.get(color="TestColor1")
        self.assertEqual(petstest1.color, 'TestColor1')
