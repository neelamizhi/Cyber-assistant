import requests

def my_ip():
    ip = requests.get("https://api.ipify.org").text
    print("Your IP:", ip)
