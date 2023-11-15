import json

import requests


def run_test():
    url = 'http://localhost:5000/get_form'
    headers = {
        'Content-type': 'application/json',
        'Accept': '*/*'
    }

    for payload in get_payloads():
        response = requests.post(url, data=json.dumps(payload), headers=headers)

        response_json = response.json()
        print(str(response_json))


def get_payloads():
    return [
        {'date_registered': '1994/08/25'},
        {'first_name': 'Daniel', 'email': 'invalid_value'},
        {'first_name': 'Daniel', 'email': 'qwe123@gmail.com', 'phone_number': '+79961234567', 'dob': '1994/08/25'},
        {'dob': '25.08.1994', 'date_registered': 'invalid_value'},
        {'email': 'qwe123@gmail.com', 'phone_number': 'invalid_value'}
    ]


if __name__ == "__main__":
    run_test()





