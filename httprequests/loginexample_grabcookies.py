import requests

print("Username and password is admin\n")

username = input("Please enter your username: ")
password = input("Please enter your password: ")

url = 'https://demo.testfire.net/doLogin'
session = requests.session()

login_payload = {
    'uid': username,
    'passw': password
}

try:
    response = session.post(url, data=login_payload)

    if response.text.__contains__('login'):
        print("Invalid username and password!")
    else:
        print("\nSuccessfully logged in as: ", username)
        print("Cookies: ", session.cookies.get_dict())
except:
    print("Cant connect to the website")
