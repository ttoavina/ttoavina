import requests
from datetime import datetime
import json

now = datetime.now()

print(f"""
<p align="left"> <img src="https://komarev.com/ghpvc/?username=ttoavina&label=Profile%20views&color=0e75b6&style=flat" alt="ttoavina" /> </p>
<h1 align="center">Hi, I'm Tokiniaina Toavina</h1>
<h3 align="center">A passionate data scientist from Madagascar</h3>
    
<hr/>
<h1> What happen this day {now.day}/{now.month} ?(Hover on the year)</h1>
""")

url = f"https://api.wikimedia.org/feed/v1/wikipedia/en/onthisday/events/{now.month}/{now.day}"
data = json.loads(requests.get(url).content)

for element in data["events"]:
    print(f"En {element['year']} : {element['text']}")
    print("<br/>"*2)



