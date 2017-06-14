from django.shortcuts import render
from django.http import HttpResponse
import requests
import pprint
import pdb
# Create your views here.

CLIENT_ID=4656
CLIENT_SECRET = 'xxx'

def home(request):
    '''root url of the site'''

    REDIRECT_URI = 'http://localhost:8000/authent'
    return render(request,"home.html",{'url':REDIRECT_URI,
                                       'clientID':CLIENT_ID,
                                       })

def authent(request):
    code = request.GET['code']
    getAccess = {'client_id':CLIENT_ID,'client_secret':CLIENT_SECRET,'code':code}
    accessTokenResp = requests.post('https://www.strava.com/oauth/token',params=getAccess)
    accessToken = accessTokenResp.json()['access_token']
    athlete = accessTokenResp.json()['athlete']
    listKOMandCRs(athlete['id'],accessToken)
    return render(request,"overview.html",{'athlete':athlete,'accessToken':accessToken})

def listKOMandCRs(id,accessToken,page=None,per_pag=None):
    overalKOMs = requests.get('https://www.strava.com/api/v3/athletes/%s/koms'%id,params='access_token=%s'%accessToken)
