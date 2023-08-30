import requests
import os

client_id=os.getenv("client_id")
client_secret=os.getenv("client_secret")
tenat_id=os.getenv("tenat_id")

def get_access_token(client_id, client_secret, tenant_id, resource='https://graph.microsoft.com'):
    url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"
    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
        'resource': resource,
    }
    response = requests.post(url, data=data)
    access_token = response.json()['access_token']
    return access_token
get_access_token(client_id,client_secret,tenat_id, resource='https://graph.microsoft.com')