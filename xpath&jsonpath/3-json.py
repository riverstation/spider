import json

lt = [
	{'name': '王静', 'age': '7', 'height': '130'},
	{'name': '闫晓红', 'age': '14', 'height': '163'},
	{'name': '刘慧芬', 'age': '16', 'height': '160'},
	{'name': '王美丽', 'age': '20', 'height': '168'},
]

string = json.dumps(lt, ensure_ascii=False)

obj = json.loads(string)

print(type(obj))

