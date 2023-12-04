#AP
#Using Request lib in python to make http methods
#make CRUD and verify

import requests

def main():
    response_body = requests.get("https://restful-booker.herokuapp.com/booking/1477")
    print(response_body.text)
    print(response_body.status_code)
    print(response_body.json())
    print(response_body.headers)
    if response_body.status_code == 200:
        print("request is  successful")
    else:
        print("request is not successful")


if __name__ == "__main__":
    main()
