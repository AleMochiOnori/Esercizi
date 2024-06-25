import unittest
from unittest import TestCase
from persona import Persona
from Dottore import Dottore

class TestPersona(unittest.TestCase):
    def setUp(self):
        self.persona = Persona('Mario', 'Rossi')

    def test_initalization(self):
        self.assertEqual(self.persona.getName() ,  "Mario")
        self.assertEqual(self.persona.last_name , "Rossi")
        self.assertEqual(self.persona.età , 0)



    def test_set_first_name(self):
        self.persona.setName("Flavio")
        self.assertEqual(self.persona.first_name , "Flavio")


    def test_set_last_name(self):
        self.persona.setLastName("Cikolin")
        self.assertEqual(self.persona.last_name , "Cikolin")

    def test_set_age(self):
        self.persona.setAge(32)
        self.assertEqual(self.persona.età , 32)


if __name__ == '__main__':
    unittest.main()



class TestDottore(unittest.TestCase):
    def setUp(self):
        self.dottore = Dottore("Alice","Cafagna","Oncrinologa",1200)
        