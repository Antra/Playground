import requests
import json
import pandas as pd
#import pyodbc
import os


# Application Id - on the azure app overview page
app_id = os.getenv('app_id')
client_secret = os.getenv('client_secret')
username = os.getenv('username')
password = os.getenv('password')


# Use the redirect URL to create a token url
#token_url = 'https://login.microsoftonline.com/371acba8-eec3-4163-abe5-606c4b32be3e/oauth2/token'
token_url = 'https://login.microsoftonline.com/common/oauth2/token'

token_data = {"grant_type": "client_credentials", # authorization_code or client_credentials
              "client_id": app_id,
              "client_secret": client_secret,
              "resource": "https://graph.microsoft.com",
              "scope": "https://graph.microsoft.com/.default",
              "username": username,
              "password": password
              }
token_r = requests.post(token_url, data=token_data)
token = token_r.json().get('access_token')

print(token)


# And with the Auth path instead
token_url = 'https://login.microsoftonline.com/common/oauth2/v2.0/authorize'

token_data = {
    "grant_type": "authorization_code",
    "client_id": app_id,
    "client_secret": client_secret,
    "scope": "https://graph.microsoft.com/.default",
}

# Called manually:
# https://login.microsoftonline.com/371acba8-eec3-4163-abe5-606c4b32be3e/oauth2/v2.0/authorize?client_id=b181eb75-ab93-461c-ad82-79039bba7f41&response_type=code&scope=https%3A%2F%2Fgraph.microsoft.com%2F.default

# then got a return URL with the below:
token_code = "0.ATEAqMsaN8PuY0Gr5WBsSzK-PnXrgbGTqxxGrYJ5A5u6f0ExANA.AQABAAIAAAAm-06blBE1TpVMil8KPQ41EIlnZWty2-p39NNUBf-eUmQ1nQUeMKIStT4VBcMCEEauj_4w1kXXdfuC_mGul4z_aOuMHkaR2dkTRsGEXhUYky542e1lS0a8m35Ye9nkJ-Or9QjJwffLOWQYt_y-pZA9tp9GL2zevmYDsUmIviqZr5BSo4oD4h38MjnJbR2RyNelxbNktS-eOiCTQkLHcN8HBHNjgpKDrXaMbfqWaRuR9PMXz0U64nkpnPD40SwlvzPo8TFqSmrIy98CoZKnTytX6_ZVVXMK_Dn0SpaqYJfOUx-_4tBPv-6llUSDPXfg5GOdgkvXiZ_7pUjpjfZ60pQ2MWEBQnH0hPG_9ri9EFHiTTUaG_SiW4sCLS8Gn0m7Wtzrie5U_FntJnQk52hTHt0WzzH2rPsXlS5fSFS1fXDNNoFEdmc0jPP7cZIEJV70yw7RgefAoTWfd-kUavCYXyor8wQ6aRoRIL6Ce26FdDjIrTxKJ8wd2d2m7wSH-N6EjZelp5QEq_XaFf30_2MdiHAhhGIVoRIHHxWnZoMWEEeIcXtmhJb6cx6fnsEiR8R-femhQSmoWH-9oWQSZHGuDz6dxZxs8K2582PzjTEvENB8jqRkSciqE0lzasTI0_ZKshpOMkhIqcuCiZWKFoJBFPLGP1hzFzIOWPHe9_cbTWuQtzGhU8u59xLNCvn7lmbN9Rs7gzvyTqWmgrGJX4k1g0dS9__8DY_IIv4AMQMLgdJVKeeLEz1gBAaImiLeNg0XiiCZp1QvIRikgf34V7nKikgdlE99L87vWm_v_2IphWHj1kfgQv0wlsjDelqD5MsMX85F6hkAHttG-opkmjOv8pr-cDkdMG7NtHd1mB1M-Gy1z_GhJnJ4gLtzDrc2R-yGYVZCZpo-M0VIX1Fpf8Y9vqtMKNm0i9iCap_je7Yy2iUloNp41YjFR2lCaVH5vNstjiuydplOAEjKkBykOzxqHI9dexyVshM8KF9_uAQRIJykHc7NnUTTIMlQbmMvDzOL4JcGDOZjFficINGi8JIZymLZzYkdvPEQfQAYGNVLJGEYKELl-G_qdzs0UhrkXW520RdDbqxpr5XExvldQzPzlx32PYQt9BxWhhH6Ucim35dfYlh7IQgpRC5dIxORPeLzvVEgAA"
token_session_state = "25f7b9f8-71eb-4b2a-920c-9d57b016ad78"

token_url = 'https://login.microsoftonline.com/371acba8-eec3-4163-abe5-606c4b32be3e/oauth2/token'

token_data = {
    "grant_type": "authorization_code", # authorization_code or client_credentials
    "client_id": app_id,
    "client_secret": client_secret,
    "code": token_code,
    "scope": "https://graph.microsoft.com/.default",
}

token_r = requests.post(token_url, data=token_data)
token = token_r.json().get('access_token')

token = 'eyJ0eXAiOiJKV1QiLCJub25jZSI6IjhLYUxHaW1odlE1TVg1ZzZSemw3VzVMSlpnTmZmR0IwZDdNVEZaVl9WYWMiLCJhbGciOiJSUzI1NiIsIng1dCI6IllNRUxIVDBndmIwbXhvU0RvWWZvbWpxZmpZVSIsImtpZCI6IllNRUxIVDBndmIwbXhvU0RvWWZvbWpxZmpZVSJ9.eyJhdWQiOiJodHRwczovL2dyYXBoLm1pY3Jvc29mdC5jb20iLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8zNzFhY2JhOC1lZWMzLTQxNjMtYWJlNS02MDZjNGIzMmJlM2UvIiwiaWF0IjoxNTg1NzU3ODQyLCJuYmYiOjE1ODU3NTc4NDIsImV4cCI6MTU4NTc2MTc0MiwiYWlvIjoiNDJkZ1lMRFZ1Sk1UcEhqY2I4ZU8yb3ViYzZkK0FnQT0iLCJhcHBfZGlzcGxheW5hbWUiOiJQeUFzc2lzdGVkSW52ZW50b3J5IChQQUkpIiwiYXBwaWQiOiJiMTgxZWI3NS1hYjkzLTQ2MWMtYWQ4Mi03OTAzOWJiYTdmNDEiLCJhcHBpZGFjciI6IjEiLCJpZHAiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8zNzFhY2JhOC1lZWMzLTQxNjMtYWJlNS02MDZjNGIzMmJlM2UvIiwib2lkIjoiNGQzYmJhNDYtN2I5Yy00OWY3LThkZjMtYjAwZWRiMTZlOWY0Iiwicm9sZXMiOlsiVXNlci5SZWFkLkFsbCJdLCJzdWIiOiI0ZDNiYmE0Ni03YjljLTQ5ZjctOGRmMy1iMDBlZGIxNmU5ZjQiLCJ0aWQiOiIzNzFhY2JhOC1lZWMzLTQxNjMtYWJlNS02MDZjNGIzMmJlM2UiLCJ1dGkiOiJjVVo5bkxzVHprdUxIbHBfOURFS0FBIiwidmVyIjoiMS4wIiwieG1zX3RjZHQiOjE1NDY3OTg3Njd9.UeNhk_7LLLK_qMN1qS9mHzPnHzmCqmitPjd6B3m2kg5G1Oc8n9limCzeLBRIJNFvE4l66u6wFkDWhPAt8b3k-z8UsauBKC-BGEt7HIw_6oF3jcxIzboXAXentUDrzmPc1B4uhnlECarH8lslFSgksUD2FGA95ncOefcV19N4clJs1FWLX_C7tDou_1dKXS5X4pQGv6PmAA4VSb9KXE7jAAn76slkNWMH8WJ8C5WdZlpvYXHDqhHUkLA3xFMf44_6f-bXivz2mi9LSahuEQJNUZOfvmJPVLJBx_Cxhn6-93Wo-YhZS_Ph4VqGaIrmGW_gHCP3Q_SoNzzLhM9osgZjpg'

headers = {
    'Authorization': f'Bearer {token}'
}

# Get Tasks
tasks_url = 'https://graph.microsoft.com/beta/me/outlook/tasks'

tasks_response_data = json.loads(requests.get(tasks_url, headers=headers).text)
print("Tasks response data:", tasks_response_data)


# define required lists
userId, displayName, mailAddress, plans_data, planId, PlanGrpOwnerId, PlanTitle, PlanCreatedBy, bucketId, bucketName, bucketPlanId, taskId, taskPlanId, taskBucketId, taskName, taskPercentComplete, taskStartDateTime, taskDueDateTime, taskCompleteDateTime, taskIdAssignment, taskUserIdAssignment = [
], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []


# Use the token using microsoft graph endpoints
users_url = 'https://graph.microsoft.com/v1.0/users?$top=500'
user_response_data = json.loads(requests.get(users_url, headers=headers).text)

print("User response data:", user_response_data)

for user in user_response_data['value']:
    userId.append(user['id'])
    displayName.append(user['displayName'])
    mailAddress.append(user['userPrincipalName'])

users_dict = {'userId': userId,
              'displayName': displayName, 'mailAddress': mailAddress}
users_df = pd.DataFrame(data=users_dict)

tasks_url = 'https://graph.microsoft.com/beta/users/6d303645-446d-442e-8e21-920cb2722f82/outlook/tasks'

tasks_response_data = json.loads(requests.get(tasks_url, headers=headers).text)

print(tasks_response_data)

