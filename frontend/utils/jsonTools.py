import json

def list_all_json(data):
    data = json.dumps(data, indent=4, default=str)
    return json.dumps(data, indent=4, default=str)