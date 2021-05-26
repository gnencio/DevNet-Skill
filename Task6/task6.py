import requests
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder

access_token = 'my_token'

headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}

# Create a space/room
url_rooms = 'https://webexapis.com/v1/rooms'
params_title={'title': 'netacad_devasc_skills_GN'}
res_create = requests.post(url_rooms, headers=headers, json=params_title)

room_id=res_create.json()['id']

# Add member to the room
person_email = 'atoxopeu@cisco.com'
url_member = 'https://webexapis.com/v1/memberships'
params_member = {'roomId': room_id, 'personEmail': person_email}
res_member = requests.post(url_member, headers=headers, json=params_member)

# Send message on GitHub remote repository
message_git = 'Hi Arjan! My GitHub remote repo is: https://github.com/gnencio/Devasc_Skill.git'
url_message = 'https://webexapis.com/v1/messages'
params_git = {'roomId': room_id, 'markdown': message_git}
res_git = requests.post(url_message, headers=headers, json=params_git)

# Send message with screenshot Task 1
message_scr = 'Here are my screenshots of netacad-devasc skills-based exam'
params_scr = MultipartEncoder({'roomId': room_id,
                              'text': message_scr,
                              'files': ('/home/devasc/Devasc_Skill/Screenshots/Task1.png', open('/home/devasc/Devasc_Skill/Screenshots/Task1.png', 'rb'), 'image/png')
                            })
headers_scr = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': params_scr.content_type
}
res_scr = requests.post(url_message, headers=headers_scr, data=params_scr)

# Send screenshot Task 2
params_scr2 = MultipartEncoder({'roomId': room_id,
                              'files': ('/home/devasc/Devasc_Skill/Screenshots/Task2.png', open('/home/devasc/Devasc_Skill/Screenshots/Task2.png', 'rb'), 'image/png')
                            })
headers_scr2 = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': params_scr2.content_type
}
res_scr2 = requests.post(url_message, headers=headers_scr2, data=params_scr2)

# Send screenshot Task 3
params_scr3 = MultipartEncoder({'roomId': room_id,
                              'files': ('/home/devasc/Devasc_Skill/Screenshots/Task3.png', open('/home/devasc/Devasc_Skill/Screenshots/Task3.png', 'rb'), 'image/png')
                            })
headers_scr3 = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': params_scr3.content_type
}
res_scr3 = requests.post(url_message, headers=headers_scr3, data=params_scr3)

# Send screenshot Task 4
params_scr4 = MultipartEncoder({'roomId': room_id,
                              'files': ('/home/devasc/Devasc_Skill/Screenshots/Task4.png', open('/home/devasc/Devasc_Skill/Screenshots/Task4.png', 'rb'), 'image/png')
                            })
headers_scr4 = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': params_scr4.content_type
}
res_scr4 = requests.post(url_message, headers=headers_scr4, data=params_scr4)

# Send screenshot Task 5
params_scr5 = MultipartEncoder({'roomId': room_id,
                              'files': ('/home/devasc/Devasc_Skill/Screenshots/Task5.png', open('/home/devasc/Devasc_Skill/Screenshots/Task5.png', 'rb'), 'image/png')
                            })
headers_scr5 = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': params_scr5.content_type
}
res_scr5 = requests.post(url_message, headers=headers_scr5, data=params_scr5)

# Send screenshot Task 7
params_scr7 = MultipartEncoder({'roomId': room_id,
                              'files': ('/home/devasc/Devasc_Skill/Screenshots/Task7.png', open('/home/devasc/Devasc_Skill/Screenshots/Task2.png', 'rb'), 'image/png')
                            })
headers_scr7 = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': params_scr7.content_type
}
res_scr7 = requests.post(url_message, headers=headers_scr7, data=params_scr7)