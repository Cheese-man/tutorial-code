#!/usr/bin/env python3

# HAAS v1 sample code
from requests import Session
import re

s = Session()

# s.cert = "path/to/your/cert/pemfile/z5555555.pem"
# The above and 2 below lines are mutually exclusive!
s.verify = False
s.proxies = {"https": "http://127.0.0.1:8080"}

def example():
    # You can use the function below to test if you can make requests
    r = s.get("https://whoami.quoccacorp.com")
    print(r.content)

def haasV1():
    URL = "https://haas-v1.quoccacorp.com"

    request_box_headers = [
        f"GET /simple HTTP/1.1",
        "Host: kb.quoccacorp.com",
        "\r\n"
    ]
    request_box = "\n".join(request_box_headers)

    res = s.post(URL, data={ "requestBox": request_box })
    # The line below is just a fancier way of doing something like this:
    # > response = res.content.split(b'\r\n\r\n')
    # > headers = response[0]
    # > body = response[-1]
    headers, *_, body = res.content.split(b'\r\n\r\n')
    print(headers, body)

    # Note here about the regex - the brackets define a 'capture group',
    # since there's only one capture group, findall will return an array of strings
    # that matches the group (e.g. ['simple/loans', 'simple/'])
    endpoint_matches = re.findall('="(simple/.*)"', body.decode())
    
    print(endpoint_matches)
    # You should be able to use the sample code to complete the rest of the function :)

if __name__ == "__main__":
    # example()
    haasV1()