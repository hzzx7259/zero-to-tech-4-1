import json

site_name = "zero-to-tech-4-1"

def make_data():
    data = {"message": "hello, world", "from": site_name}
    return json.dumps(data)

print(make_data())
