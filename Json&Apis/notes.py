'''Reading JSON with the loads() Function'''
stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'

import json
jsonDataAsPythonValue = json.loads(stringOfJsonData)
print(jsonDataAsPythonValue)
print(type(jsonDataAsPythonValue))


'''Writing JSON with the dumps() Function'''
pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}

stringOfJsonData2 = json.dumps(pythonValue)
print(stringOfJsonData2)
print(type(stringOfJsonData2))


heroes = {
    "Superman": "Clark Kent",
    "Batman": "Bruce Wayne",
    "stats": {"total_views": 1800, "videos": [{"name": "Threading Basics in C",
    "likes": 15,
    "dislikes": 1,
    "views": 498}]}
    }

print(heroes)
print()
print(heroes["stats"]["total_views"])
print(heroes["stats"]["videos"])
print(type(heroes["stats"]["videos"]))

for video in heroes["stats"]["videos"]:
    print(video["name"])
    print(video["likes"])
    print(video["dislikes"])
    print(video["views"])
