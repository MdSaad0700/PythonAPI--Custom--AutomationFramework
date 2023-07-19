import json


def get_payload_auth():
    file_data = open("resource/constant/auth.json")
    data = json.loads(file_data)
    file_data.close()
    return data
