from django.shortcuts import render
import os
from django.shortcuts import redirect, render
from urllib.parse import urlencode

def index(request):
    # Construct the authorization URL
    authorization_url = "https://login.microsoftonline.com/common/oauth2/v2.0/authorize"
    client_id = os.getenv("client_id")
    redirect_uri = "http://localhost:8000/callback/"
    scope = "Files.ReadWrite"
    
    params = {
        "client_id": client_id,
        "response_type": "code",
        "redirect_uri": redirect_uri,
        "scope": scope
    }
    
    authorization_url = authorization_url + "?" + urlencode(params)
    
    return redirect(authorization_url)

import requests

def callback(request):
    # Retrieve the authorization code from the query parameters
    authorization_code = request.GET.get('code')
    
    
    # Use the authorization code to obtain an access token
    # (Implement the code to exchange the authorization code for an access token)
    
    return render(request, 'callback.html', {'authorization_code': authorization_code})

