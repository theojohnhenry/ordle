# improvements:
# use kellylist dataset to use more frequently used words as this shit comes up with some weird ass words

import json

with open("svenska-ord.json","r") as f:
    data = json.load(f)

def generate5WordFile(data):
    newData = [word.lower() for word in data if len(word) == 5 and (" " not in word) and ("-" not in word)]
    with open("sample.json", "w") as outfile:
        json.dump(newData, outfile, ensure_ascii=False)

