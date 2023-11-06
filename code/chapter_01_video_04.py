import pandas as pd
import requests

link = "https://3083218.youcanlearnit.net/dataTable.html"

# response = requests.get("https://3083218.youcanlearnit.net/rank.json?_=1662342121475")
# response = requests.get("https://3083218.youcanlearnit.net/rank.json?_=1699021114780")
state_data = pd.read_json("https://3083218.youcanlearnit.net/rank.json?_=1699021114780")
# state_data = pd.read_json(response.content)
# state_data = json.loads(response.read().decode('utf-8'))
state_data = pd.DataFrame(state_data['data'].to_list(), columns = ['rank', 'state', 'rainfall'])
