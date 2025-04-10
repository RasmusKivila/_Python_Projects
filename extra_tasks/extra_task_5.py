# Vilken post (https://dummyjson.com/docs/posts) har fått flest kommentarer?

import requests

api_url = "https://dummyjson.com/posts?limit=150"
response_json = requests.get(api_url).json()
posts = response_json['posts']

for post in posts:
    post_id = post['id']
    api_url = f"https://dummyjson.com/posts/{post_id}/comments"
    response_json = requests.get(api_url).json()
    comments = response_json['comments']
    post['comments_count'] = len(comments)

max_reacts_post = max(posts, key=lambda post:post['comments_count'])

print(max_reacts_post)