from app import app
import json

class TestListUsers(self):
    def test_get_all_users(self):

        #Arrange
        UserFactory.create[{
            "name": "Jorge",
            "apellido": "Gonzales",
            "edad": 34
        }]
        

        #Act
        response = app.test_client().get('/users')

        #Assert
        assert response.status_code == 200
        parsed_data = json.loads(response.data.decode('utf-8'))
        assert parsed_data == [{
            "name": "Jorge",
            "apellido": "Gonzales",
            "edad": 34
        }]



