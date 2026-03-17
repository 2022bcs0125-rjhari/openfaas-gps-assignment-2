import requests
import json

def handle(req):
    try:
        res = requests.get("http://ip-api.com/json")
        data = res.json()

        return json.dumps({
            "name": "R J Hari",
            "roll_number": "2022BCS0125",
            "latitude": data.get("lat"),
            "longitude": data.get("lon"),
            "city": data.get("city"),
            "country": data.get("country"),
            "status": "success"
        })

    except Exception as e:
        return json.dumps({"error": str(e)})