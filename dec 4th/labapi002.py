#Assertion - verify the expected result with actual result
import requests

def main():
    id = 1477
    url = "https://restful-booker.herokuapp.com/booking/"
    full_url = url + str(id)
    print(full_url)
    response_body = requests.get(full_url)
    assert response_body.status_code == 200 # if sc != 200 its error or it works

if __name__ == '__main__':
    main()