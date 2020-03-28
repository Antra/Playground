import requests
import json
import pandas as pd
#import pyodbc


# Application Id - on the azure app overview page
app_id = 'b181eb75-ab93-461c-ad82-79039bba7f41'
client_secret = 'secret'


# Use the redirect URL to create a token url
token_url = 'https://login.microsoftonline.com/371acba8-eec3-4163-abe5-606c4b32be3e/oauth2/token'


token_data = {"grant_type": "client_credentials",
              "client_id": app_id,
              "client_secret": client_secret,
              "resource": "https://graph.microsoft.com",
              "scope": "https://graph.microsoft.com/.default",
              "username": "ABC",
              "password": "****"
              }
token_r = requests.post(token_url, data=token_data)
token = token_r.json().get('access_token')


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
    "grant_type": "authorization_code",
    "client_id": app_id,
    "client_secret": client_secret,
    "code": token_code,
    "scope": "https://graph.microsoft.com/.default",
}

token_r = requests.post(token_url, data=token_data)
token = token_r.json().get('access_token')

token = 'eyJ0eXAiOiJKV1QiLCJub25jZSI6IktYb01VUnNUQ3dTTGhFcE9ObldIRGZYRUVTU0xKVm9LTEpJcVhiZVNmeXMiLCJhbGciOiJSUzI1NiIsIng1dCI6IllNRUxIVDBndmIwbXhvU0RvWWZvbWpxZmpZVSIsImtpZCI6IllNRUxIVDBndmIwbXhvU0RvWWZvbWpxZmpZVSJ9.eyJhdWQiOiJodHRwczovL2dyYXBoLm1pY3Jvc29mdC5jb20iLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8zNzFhY2JhOC1lZWMzLTQxNjMtYWJlNS02MDZjNGIzMmJlM2UvIiwiaWF0IjoxNTg1MTY4OTAyLCJuYmYiOjE1ODUxNjg5MDIsImV4cCI6MTU4NTE3MjgwMiwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFUUUF5LzhQQUFBQU5sSC9EWVR5ZnFhMGo1Z1BoT3BHQTc0WWJsSDBRRTRGTzAzaWV2SkVHTkowZmhhTnhvdk1lYVN5RHZUWGM5OGEiLCJhbHRzZWNpZCI6IjE6bGl2ZS5jb206MDAwMzdGRkU5MzAyQ0MyMiIsImFtciI6WyJwd2QiXSwiYXBwX2Rpc3BsYXluYW1lIjoiUHlBc3Npc3RlZEludmVudG9yeSAoUEFJKSIsImFwcGlkIjoiYjE4MWViNzUtYWI5My00NjFjLWFkODItNzkwMzliYmE3ZjQxIiwiYXBwaWRhY3IiOiIxIiwiZW1haWwiOiJ4Ym94QGFudHJhLmRrIiwiZmFtaWx5X25hbWUiOiJEZW1hbnQgdmFuIGRlciBXZWlkZSIsImdpdmVuX25hbWUiOiJBbmRlcnMiLCJpZHAiOiJsaXZlLmNvbSIsImlwYWRkciI6IjIxMi4yMzcuMTM0LjEwMSIsIm5hbWUiOiJBbmRlcnMgRGVtYW50IHZhbiBkZXIgV2VpZGUiLCJvaWQiOiI2ZDMwMzY0NS00NDZkLTQ0MmUtOGUyMS05MjBjYjI3MjJmODIiLCJwbGF0ZiI6IjMiLCJwdWlkIjoiMTAwMzIwMDAzNjcwNUZCOSIsInNjcCI6IkNhbGVuZGFycy5SZWFkLlNoYXJlZCBvZmZsaW5lX2FjY2VzcyBUYXNrcy5SZWFkIFRhc2tzLlJlYWQuU2hhcmVkIFRhc2tzLlJlYWRXcml0ZSBUYXNrcy5SZWFkV3JpdGUuU2hhcmVkIFVzZXIuUmVhZCIsInNpZ25pbl9zdGF0ZSI6WyJrbXNpIl0sInN1YiI6IlJpVF9vNzlBTmZHTF9wN1RpSUhrY2JQX29BV3QyZ25vQk52TEdDZFV4M00iLCJ0aWQiOiIzNzFhY2JhOC1lZWMzLTQxNjMtYWJlNS02MDZjNGIzMmJlM2UiLCJ1bmlxdWVfbmFtZSI6ImxpdmUuY29tI3hib3hAYW50cmEuZGsiLCJ1dGkiOiJmSUdnb1daUXhVR1RQdUU0aG5jQUFBIiwidmVyIjoiMS4wIiwid2lkcyI6WyI2MmU5MDM5NC02OWY1LTQyMzctOTE5MC0wMTIxNzcxNDVlMTAiXSwieG1zX3RjZHQiOjE1NDY3OTg3Njd9.URVmUYgk4_SLrPufElkrD8SWUTYyIMzxtyuGq5emzqZkA5hLJuLCsUCjOiImFR6kR6gboJbOypQXHIEzIAfnDaMliCRvFu4GCUkcBisEtNKU62dnoNs3WC2HRs0N-YQGmrgTSUYXQvtlZ6YIRuGutfcKgPEv8CTEdA7roOoKi8MJxVvZZrQvbaXknznUM4vGUAqHyM47d83lW7L8qRm6ydx_RiF28FNX3mirOtQfI5NesJoZkNKU2Mh6szMO4E53wqn1wHxU16KxuMfXHAnvxO098f-1xdem6wFpmeSrwhXd--cYEIS6RhB3IAHB23aNTyfWx3ZEmmwfShbnJ9pUSw'

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
