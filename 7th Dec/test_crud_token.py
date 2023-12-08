import requests


def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=url, headers=headers, json=json_payload)
    data = response.json()
    token = data["token"]
    print(token)
    return token


def create_booking():
    print('create booking testcase')
    URL = "https://restful-booker.herokuapp.com/booking"
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
    booking_id = data["bookingid"]
    return booking_id


def test_put_request():
    URL = "https://restful-booker.herokuapp.com/booking/"
    booking_id = create_booking()
    PUT_URL = URL + str(booking_id)
    cookie_value = "token=" + create_token()
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie_value
    }
    print(headers)
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
    response = requests.put(url=PUT_URL, headers=headers, json=json_payload)
    assert response.status_code == 200
    # get the response and verify the json, booking id is none
    data = response.json()
    print(data)
    assert data["firstname"] == "Jim", "Failed msg-Incorect firstname"


def test_delete():
    try:
        url = "https://restful-booker.herokuapp.com/booking"
        booking_id = create_booking()
        put_url = url + str(booking_id)
        cookie_value = "token=" + create_token()
        headers = {
            "Content-Type": "application/json",
            "Cookie": cookie_value
        }
        print(headers)

        response = requests.delete(url=put_url, headers=headers)
        assert response.status_code == 201
    # get the response and verify the json, booking id is none

    except Exception as e:
        print(e)
