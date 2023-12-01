import requests
import pytest

session = requests.session()

def register_user(name, LastName, email, password, repeatPassword):
    url = "https://qauto2.forstudy.space/api/auth/signup"
    data = {
        "name": name,
        "LastName": LastName,
        "email": email,
        "password": password,
        "repeatPassword": repeatPassword
    }
    response = session.post(url=url, json=data
    return print(response)


register_user("Zaraki", "Kenpache", "testho4mewok11@gmail.com", "Qwerty12345", "Qwerty12345")
#Параметризований тест для реєстрації юзера
@pytest.mark.parametrize("name,LastName,email,password,repeatPassword, expected_status_code",
                        [
                            ("Zaraki", "Kenpache", "testho4mewok11@gmail.com", "Qwerty12345", "Qwerty12345", 201),
                            ("Vol", "Wat", "testhomework22@gmail.com", "Qwerty12345", "Qwerty12345", 201),
                            ("l", "password456", "testhomework33@gmail.com", "33", "33", 400),
                        ])
def test_user_registration(name, LastName, email, password, repeatPassword, expected_status_code):
    response = register_user(name, LastName, email, password, repeatPassword)
    assert response.status_code == expected_status_code
