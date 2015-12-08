from django.shortcuts import render
from django.http import HttpResponse
import requests
import pprint
import pdb
# Create your views here.

CLIENT_ID=4656
CLIENT_SECRET = '9b75ee6abf3f44d7b6f48b7cd9ef6d89dad72090'
def home(request):
    '''root url of the site'''

    REDIRECT_URI = 'http://localhost:8000/authent'
    print REDIRECT_URI
    return HttpResponse("""<a href="https://www.strava.com/oauth/authorize?client_id=%s&response_type=code&redirect_uri=%s&scope=write&state=fromroot&approval_prompt=auto">click to connect</a>"""%(CLIENT_ID,REDIRECT_URI))

def authent(request):
    code = request.GET['code']
    getAccess = {'client_id':CLIENT_ID,'client_secret':CLIENT_SECRET,'code':code}
    accessTokenResp = requests.post('https://www.strava.com/oauth/token',params=getAccess)
    accessToken = accessTokenResp.json()['access_token']
    athlete = accessTokenResp.json()['athlete']
    return render(request,"overview.html",{'athlete':athlete})

def list_friends(athlete,accesstoken):
    """ list all friends """
    pass
