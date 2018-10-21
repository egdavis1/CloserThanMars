#Written by: Sam Dugan and Justin Drapeau
import json
import os
import requests

CONST = "data.txt"
CONST1 = "TheWayYouNibbleOnMyEarTheOnlyWordsIWannaHear.txt"

x1 = open(CONST, "r")
x2 = open(CONST1, "r")

y1 = json.loads(x1.read())
y2 = json.loads(x2.read())

print("Proccessing files.")

c = 0
z = ["color", "description", "categories"]

for b in y1["images"]:
    if y2["images"][c]["metadata"]["format"] == "Jpeg":
        for a in z:
            y1["images"][c][a] = y2["images"][c][a]
        if y1["images"][c]["description"]["captions"] == []:
            y1["images"][c]["description"]["captions"] = [{"confidence": 1,"text": "unknown"}]
        y1["images"][c]["description"]["confidence"] = y1["images"][c]["description"]["captions"][0]["confidence"]
        y1["images"][c]["description"]["text"] = y1["images"][c]["description"]["captions"][0]["text"]
        del y1["images"][c]["description"]["captions"]

        payload_dict = {'data': json.dumps(y1["images"][c])}
        r2 = requests.post('http://e9bf61d8.ngrok.io/api/upload/image', data=payload_dict)
        print("Line ", c, " success ", r2)
    else:
        print("Error on line ", c)
    c += 1
    
x1.close()
x2.close()

os.remove(CONST)
os.remove(CONST1)

