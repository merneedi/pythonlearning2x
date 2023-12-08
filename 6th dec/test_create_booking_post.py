# Python testing framework - Unit test, nose, pytest(popular)(TestNG)
# 2.Every test will satrt from test_name.py
# 3.pytest -h
# 4.pytest -k-> match substring => pytest -k 'name => test_name.py
# 5.pytst -v logs
import pytest
# How to create the booking by using pytest-> allure
import requests


@pytest.mark.positive
def test_create_booking_positive():
    print('create booking testcase')
    URL = "https://restful-booker.herokuapp.com/booking/"
    Headers = {"Content-Type": "application/json"}
    json_payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL, headers=Headers, json=json_payload)
    print(type(URL))
    print(type(Headers))
    print(type(json_payload))

    # Assertions
    assert response.status_code == 200
    # get the response and verify the json, booking id is none
    data = response.json()
    print(data)
    assert data["bookingid"] is not None
    assert data["booking"]["firstname"] == "Jim", "Failed msg-Incorect firstname"


@pytest.mark.negative
def test_create_booking_negative():
    print('create booking testcase')
    URL = "https://restful-booker.herokuapp.com/booking/"
    Headers = {"Content-Type": "application/json"}
    json_payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL, headers=Headers, json=json_payload)
    print(type(URL))
    print(type(Headers))
    print(type(json_payload))

    # Assertions
    assert response.status_code == 500
