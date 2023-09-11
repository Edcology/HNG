from django.shortcuts import render
from django.http import JsonResponse
import requests
import time
from datetime import datetime
import pytz
def get_user_info(request):
    # Slack API token
    api_token = "xoxp-5525350307635-5861483270790-5879889706050-ed0126cdcde79244d36c0f7508ce40e4"

    # User's Slack name
    slack_name = "U05RKA1QMFF"
    track = "profile"

    # Construct the Slack API endpoint URL with the "user_id" parameter
    url = "https://slack.com/api/users.info"

    headers = {
        "Authorization": f"Bearer {api_token}",
    }

    params = {
        "user": slack_name,
        "status": track
    }

    # Send the GET request to retrieve user information
    request = requests.get(url, headers=headers, params=params)

    if request.status_code == 200:
        # Parse the JSON response
        user_info = request.json()
        print(user_info)

        # Extract the user's name or presence based on the track
        if user_info["ok"]:
            if track == "profile":
                user_name = user_info["user"]["profile"]["real_name"]
                user_track = user_info["user"]["profile"]["title"]
                print(f"The user's Slack name is: {user_name}")
                print(f"The user's Track is: {user_track}")
            elif track == "presence":
                user_presence = user_info["user"]["presence"]
                print(f"The user's presence is: {user_presence}")
            else:
                print(f"Invalid track: {track}")
        else:
            print(f"Error: {user_info['error']}")

    else:
        print(f"Error: {request.status_code}, {request.text}")

    def current_day():
        t = (2015, 12, 31, 10, 39, 45, 1, 48, 0)
        t = time.mktime(t)
        return(time.strftime("%A",time.localtime(t)))
    
    current_day = current_day()

    def current_utc_time():
        current_utc_time = datetime.utcnow()
        utc_timezone = pytz.timezone('UTC')
        current_utc_time = utc_timezone.localize(current_utc_time)
        utc_time_string = current_utc_time.strftime('%Y-%m-%dT%H:%M:%SZ')
        return(utc_time_string)
    
    current_utc_time = current_utc_time()  
    # Getting GitHub URL of the file being run
    github_file_url = 'https://github.com/Officialbabs/learning_with_HNG/blob/main/myproject/myapp/views.py'  
    # Getting GitHub URL of the full source code
    github_source_url = 'https://github.com/Edcology/HNG/tree/main'
    # The response JSON
    request = {
        'slack_name': user_name,
        'current_day': current_day,
        'current_utc_time': current_utc_time,
        'track': user_track,
        'github_file_url': github_file_url,
        'github_source_url': github_source_url,
        'status_code': request.status_code
    }
    return( JsonResponse(request))
