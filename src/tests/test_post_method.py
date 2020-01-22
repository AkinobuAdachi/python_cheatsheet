import requests

r = requests.post(
    'http://0.0.0.0:5000/method/post', data={'username': 'Post'}
)

# r = requests.put(
#     'http://0.0.0.0:5000/method/post', data={'username': 'put'}
# )

# r = requests.delete(
#     'http://0.0.0.0:5000/method/post', data={'username': 'delete'}
# )

# r = requests.get(
#     'http://0.0.0.0:5000/method/post', data={'username': 'get'}
# )
print(r.text)