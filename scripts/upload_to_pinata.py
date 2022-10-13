import os
from pathlib import Path
import requests


pinata_base_url = "https://api.pinata.cloud/"
endpoint = "pinning/pinFileToIPFS"
file_path = "./img/pug.png"
file_name = file_path.split("/")[-1:][0]
headers = {
    "pinata_api_key": os.getenv("PINATA_API_KEY"),
    "pinata_secret_api_key": os.getenv("PINATA_API_SECRET"),
}


def main():
    with Path(file_path).open("rb") as fp:
        image_binary = fp.read()
        response = requests.post(
            pinata_base_url + endpoint,
            files={"file": (file_name, image_binary)},
            headers=headers,
        )
        print(response.json())
