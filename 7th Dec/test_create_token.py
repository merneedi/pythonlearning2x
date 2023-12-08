import requests


def test_create_token():
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
    #return token

    # def test_put_request():
    # URL = "https://restful-booker.herokuapp.com/booking/"
    # booking_id = "3247"
    # PUT_URL = URL + (booking_id)
    # cookie_value = "token=" + create_token()
    # headers = {
    #     "Content-Type": "application/json",
    #     "Cookie": cookie_value
    # }
    # print(headers)
    # json_payload = {
    #     "firstname": "Jim",
    #     "lastname": "Brown",
    #     "totalprice": 111,
    #     "depositpaid": True,
    #     "bookingdates": {
    #         "checkin": "2018-01-01",
    #         "checkout": "2019-01-01"
    #     },
    #     "additionalneeds": "Breakfast"
    # }
    # response = requests.put(url=PUT_URL, headers=headers, json=json_payload)
    # assert response.status_code == 200
    # data = response.json()
    # assert data["firstname"] == "Jim", "Failed msg-Incorect firstname"
    #
