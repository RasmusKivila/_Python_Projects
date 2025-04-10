import requests
import shutil



def basic_get():
    api_url = "https://catfact.ninja/fact"
    response = requests.get(api_url)
    # Check if the server responded with an OK (200)
    if response.ok:
        print("GET was a Success")


def raw_data_get():
    api_url = "https://catfact.ninja/fact"
    response = requests.get(api_url)
    # Check if the server responded with an OK (200)
    if response.ok:
        print("GET was a Success")
        # The response object contains the actual response from the server as a string
        print(f"Result: {response.text}")

def json_get():
    api_url = "https://catfact.ninja/fact"
    response = requests.get(api_url)
    # Check if the server responded with an OK (200)
    if response.ok:
        # The response object can also convert the text to a json object by using json()
        response_json = response.json()
        print("GET was a Success")
        print(f"Result: {response_json}")

def save_result_in_variable_get():
    api_url = "https://catfact.ninja/fact"
    response = requests.get(api_url)
    # Check if the server responded with an OK (200)
    if response.ok:
        # Extract the json message of the response to a variable
        response_json = response.json()
        print("GET was a Success")
        print(f"Result: {response_json}")

def save_image_get():
    api_url = "https://api.memegen.link/images/afraid/i_don't_know_what_an_api_does/and_at_this_point_i'm_too_afraid_to_ask.png"
    # stream=True makes it possible to receive larger objects, such as images for example
    response = requests.get(api_url, stream=True)
    # Check if the server responded with an OK (200)
    if response.ok:
        with open("meme.png", 'wb') as f:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, f)


def not_found_get():
    api_url = "https://catfact.ninja/invalid_resource"
    response = requests.get(api_url)
    # The response object also contains the http status code
    print(f"Status code: {response.status_code}")
    print(f"Result: {response.text}")

def unauthorised_get():
    api_url = "https://api.spotify.com/v1/tracks/1"
    response = requests.get(api_url)
    # The response object also contains the http status code
    print(f"Status code: {response.status_code}")
    print(f"Result: {response.text}")
    
    