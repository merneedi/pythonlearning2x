import requests

def main():
    id = 440
    url = "https://restful-booker.herokuapp.com/booking/"
    full_url = url + str(id)
    print(full_url)
    response_body = requests.get(full_url)
    assert response_body.status_code == 200 # if sc != 200 its error or it works

    data = response_body.json()
    print(type(data))

    #Asertions
    #verification of keys
    assert 'firstname' in data, "First name"
    assert 'lastname' in data, "Lastname"

    #verification of data
    assert data["firstname"] == "Jim", "first name is Jim"
    assert data["lastname"] == "Brown", "last name is brown"
    assert data["bookingdates"] ["checkin"]== "2018-01-01", "Invalid msg"





if __name__ == '__main__':
    main()