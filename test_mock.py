import unittest
from unittest.mock import patch, MagicMock
from faker import Faker
from werkzeug.security import generate_password_hash
from services.customerAccountService import login_customer

class TestLoginCustomer(unittest.TestCase):

    @patch('services.customerAccountService.db.session.execute')
    def test_login_customer(self, mock_execute):
        faker = Faker()
        password = faker.password()
        mock_user = MagicMock()
        mock_user.id = 1
        mock_user.roles = [MagicMock(role_name='admin'), MagicMock(role_name='user')]
        mock_user.username = faker.user_name()
        mock_user.password = generate_password_hash(password)

        # Mock the query execution
        mock_result = MagicMock()
        mock_result.scalar_one_or_none.return_value = mock_user
        mock_execute.return_value = mock_result

        # Simulate the login function
        response = login_customer(mock_user.username, password)
        
        # Verify that the response status is 'success'
        self.assertEqual(response['status'], 'success')
        
        # Verify that the response contains an auth_token
        self.assertIn('auth_token', response)
        self.assertIsNotNone(response['auth_token'])

    @patch('services.customerAccountService.db.session.execute')
    def test_fail_login(self, mock_execute):
        faker = Faker()
        password = faker.password()
        mock_user = MagicMock()
        mock_user.id = 1
        mock_user.roles = [MagicMock(role_name='admin'), MagicMock(role_name='user')]
        mock_user.username = faker.user_name()
        mock_user.password = generate_password_hash(password)

        # Mock the query execution to return the user
        mock_result = MagicMock()
        mock_result.scalar_one_or_none.return_value = mock_user
        mock_execute.return_value = mock_result

        # Simulate the login function with a wrong password
        response = login_customer(mock_user.username, faker.password())

        # Verify that the response is None due to wrong password
        self.assertIsNone(response)

if __name__ == '__main__':
    unittest.main()
