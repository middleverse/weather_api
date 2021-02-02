from django.test import TestCase, Client

from . import views

# Create your tests here.
class TestWeatherApiMethod(TestCase):
    '''
    Test class for API V1
    '''
    c = Client()
    
    def test_no_city(self):
        response = self.c.get('/v1/api/?city=')
        self.assertEqual(400, response.status_code)

    def test_valid_city(self):
        response = self.c.get('/v1/api/?city=toronto')
        self.assertEqual(200, response.status_code)

    def test_non_existent_city(self):
        response = self.c.get('/v1/api/?city=my+imaginary+city')
        self.assertEqual(404, response.status_code)

    def test_invalid_string_as_city(self):
        response = self.c.get('/v1/api/?city=aaaaa-0293-857===-3-3033933039930aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        self.assertEqual(404, response.status_code)

    def test_integer_code_as_city_name(self):
        # should return a valid city for numbers 
        # less than total # of cities supported by openweathermap 
        response = self.c.get('/v1/api/?city=1234')
        self.assertEqual(200, response.status_code)

    def test_invalid_integer_code_as_city_name(self):
        # should return 404 for a number greater than 
        # total # of cities supported by openweathermap 
        response = self.c.get('/v1/api/?city=123433333333333333')
        self.assertEqual(404, response.status_code)        