import requests
import pytest

session = requests.session()

def register_user(name, lastName, email, password, repeatPassword):
    url = "https://qauto2.forstudy.space/api/auth/signup"
    data = {
        "name": name,
        "lastName": lastName,
        "email": email,
        "password": password,
        "repeatPassword": repeatPassword
    }
    response = session.post(url=url, json=data)
    return response

#Параметризований тест для реєстрації юзера
@pytest.mark.parametrize("name,LastName,email,password,repeatPassword, expected_status_code",
                        [
                            ("Zaraki", "Kenpache", "testhoy4merrrwok11@gmail.com", "Qwerty12345", "Qwerty12345", 201),
                            ("Vol", "Wat", "testhomewrrefhhork22@gmail.com", "Qwerty12345", "Qwerty12345", 201),
                            ("l", "password456", "testhomework33@gmail.com", "33", "33", 400),
                        ])
def test_user_registration(name, LastName, email, password, repeatPassword, expected_status_code):
    response = register_user(name, LastName, email, password, repeatPassword)
    assert response.status_code == expected_status_code
