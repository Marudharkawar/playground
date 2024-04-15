from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

class ProductAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

        # Create some test products
        self.product1 = Product.objects.create(name='Product 1', description='Description 1', manufacturer='Manufacturer 1', serial_number='12345', manufacture_date='2022-01-01', warranty_information='Warranty 1', category='physical', created_by=self.user, updated_by=self.user)
        self.product2 = Product.objects.create(name='Product 2', description='Description 2', manufacturer='Manufacturer 2', serial_number='67890', manufacture_date='2022-02-01', warranty_information='Warranty 2', category='digital', created_by=self.user, updated_by=self.user)

    def test_list_products(self):
        # Test listing products
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 2)  # Assuming 2 products are created in setUp

    def test_create_product(self):
        # Test creating a product
        data = {
            'name': 'New Product',
            'description': 'New Description',
            'manufacturer': 'New Manufacturer',
            'serial_number': '54321',
            'manufacture_date': '2022-03-01',
            'warranty_information': 'New Warranty',
            'category': 'physical',
        }
        response = self.client.post('/api/products/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 3)  # Assuming 3 products after creation

    def test_retrieve_product(self):
        # Test retrieving a product
        response = self.client.get(f'/api/products/{self.product1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Product 1')

    def test_update_product(self):
        # Test updating a product
        data = {
            'name': 'Updated Product',
            'description': 'Updated Description',
        }
        response = self.client.patch(f'/api/products/{self.product1.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated Product')

    def test_delete_product(self):
        # Test deleting a product
        response = self.client.delete(f'/api/products/{self.product1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 1)  # Assuming 1 product after deletion
