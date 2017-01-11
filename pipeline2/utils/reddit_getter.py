import requests
import pyperclip
import json


class Comment():

    bodies = []

    def __init__(self, json):
        data = json['data']

        self.body = data.get('body')
        self.score = data.get('score')

        if self.body is not None:

            # Add to bodies!
            Comment.bodies.append(self.body)

            # Get replies
            self.replies = []

            if data['replies'] != u'': # replies is not empty!
                replies = data['replies']['data']['children']
                self.get_replies(replies)

    def get_replies(self, replies_json):
        comments = []
        for reply in replies_json:
            comment = Comment(reply)
            comments.append(comment)
        self.replies = comments


# Get all the links
links_list = ['https://www.reddit.com/r/gaming/comments/5e6j8h/some_michael_bay_shit_going_on_right_here.json']

# Load a request and get json
res = requests.get(links_list[0])
j = json.loads(res.text)
print(j)

# Create all the comments
comments = j[1]['data']['children']
for com in comments:
    comment = Comment(com)


tempNum = 0
# Print the bodies
for i in Comment.bodies:
    print(i)
    tempNum += len(i.split(' '))
    print("\n\n")

print(len(Comment.bodies))
print(tempNum)


