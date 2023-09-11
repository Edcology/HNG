from django.shortcuts import render

# Create your views here.
import requests
from django.http import JsonResponse
from django.utils import timezone
import pytz

# Slack API token
api_token = "xoxp-5525350307635-5869341837525-5876924949570-20ceababdc60e14e43f8b45f03822353"

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
response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    # Parse the JSON response
    user_info = response.json()
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
    print(f"Error: {response.status_code}, {response.text}")
    
    
current_day = timezone.now().astimezone(pytz.timezone('UTC+2')).strftime('%A')

    # Getting current UTC time with validation of +/-2
current_utc_time = timezone.now()
valid_time_range = (timezone.now().astimezone(pytz.timezone('UTC-2')),timezone.now().astimezone(pytz.timezone('UTC+2')))
time_validity = valid_time_range[0] <= current_utc_time <= valid_time_range[1]
# Getting GitHub URL of the file being run
github_file_url = 'https://github.com/Officialbabs/learning_with_HNG/blob/main/myproject/myapp/views.py'  
# Getting GitHub URL of the full source code
github_source_url = 'https://github.com/Officialbabs/learning_with_HNG'
# The response JSON
response_data = {
    'slack_name': user_name,
    'current_day': current_day,
    'current_utc_time': current_utc_time.strftime('%Y-%m-%d %H:%M:%S %Z'),
    'track': user_track,
    'github_file_url': github_file_url,
    'github_source_url': github_source_url,
    'status_code': response.status_code
}
print( JsonResponse(response_data))