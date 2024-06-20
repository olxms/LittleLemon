from django.test import TestCase, Client

from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        Menu.objects.create(title="Dish1", price=15, inventory=500)
        Menu.objects.create(title="Dish2", price=25, inventory=50)
        Menu.objects.create(title="Dish3", price=150, inventory=5)

    def test_getall(self):
        # Make a GET request to the '/restaurant/menu/' endpoint
        response = self.client.get('/restaurant/menu/')

        # Retrieve all Menu objects from the database
        items = Menu.objects.all()

        # Serialize the items using MenuSerializer
        serializer = MenuSerializer(items, many=True)

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert that the JSON content of the response matches the serialized data
        self.assertEqual(response.json(), serializer.data)
