import json

search = {
     "difficulty": 1,
     "tag": ["crawl","vejrtrækning"],
     "equipment": [""]

}

totalscore = {}
sorted_totalscore = {}

with open("data.json", "r") as d:
     data = json.loads(d.read())
     
def GetScore():
    for key, value in data.items():
        score = 0

        if isinstance(value["difficulty"], int) and isinstance(search["difficulty"], int):
            score += abs(value["difficulty"] - search["difficulty"])

        for tag in search["tag"]:
            if tag not in value["tag"]:
                score += 5

        for equipment in search["equipment"]:
            if equipment not in value["equipment"]:
                score += 5

        totalscore[key] = score

def ConvertToDict(tuple, dict):
    for key, value in tuple:
        dict[key] = value

GetScore()
#               turple version af totalscore for at sortere den
#                      V
ConvertToDict(sorted(totalscore.items(), key=lambda item: item[1]), sorted_totalscore)

for key in sorted_totalscore:

    if key in data:
        print(f"{data[key]['name']}: {sorted_totalscore[key]}")
    else:
        print("error")








