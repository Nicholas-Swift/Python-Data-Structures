import requests
import json

def get_children(children):
    for child in children:
        child = child.get('data', {})
        body = child.get('body')
        print(body)

        new_children = child.get('replies', {}).get('data', {}).get('children', [])
        get_children(new_children)

# Get all the links
links_list = ['https://www.reddit.com/r/gaming/comments/5e6j8h/some_michael_bay_shit_going_on_right_here.json']

# Load a request and get json
res = requests.get(links_list[0])
j = json.loads(res.text)

# Get all comments
listing = j[1]

# Get children
wow = []
children = listing['data']['children']
print(len(children))
get_children(children)
