# Vilken user har kommenterat mest på posts?

import requests

api_url = "https://dummyjson.com/posts?limit=150"
response_json = requests.get(api_url).json()
posts = response_json['posts']

users_commenting = []

for post in posts:
    post_id = post['id']
    api_url = f"https://dummyjson.com/posts/{post_id}/comments"
    response_json = requests.get(api_url).json()
    comments = response_json['comments']
    comment_users = [comment['user']['id'] for comment in comments]
    users_commenting.extend(comment_users)


user_comments_count = [{'user_id':user, 'comments_count':users_commenting.count(user)} for user in users_commenting]
max_comments_user = max(user_comments_count, key=lambda user:user['comments_count'])
print(max_comments_user)