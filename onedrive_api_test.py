import requests
import os

file_path="C:\\Users\\vinayakav\\Downloads\\new_dp.jpg"
folder_path='/Documents/microsoft_api_text/'
access_token=os.getenv("access_token")
file_name="new_dp.jpg"

def upload_file_to_onedrive(file_path, file_name,folder_path, access_token, drive_id='me', ):
    # url = f"https://graph.microsoft.com/v1.0/{drive_id}/drive/root:{folder_path}/{file_name}:/content"
    url = f"https://ults-my.sharepoint.com/personal/vinayak_av_ultsglobal_com/Documents/{file_name}:/content"
    headers = {
        'Authorization': f'Bearer {access_token}',
    }
    with open(file_path, 'rb') as file:
        response = requests.put(url, headers=headers, data=file)
    if response.status_code == 200:
        print("File uploaded successfully.")
    else:
        print("Failed to upload file.")
        print(response.text)
    return response

# https://ults-my.sharepoint.com/personal/vinayak_av_ultsglobal_com/Documents/microsoft_api_text
upload_file_to_onedrive(file_path,file_name,access_token,folder_path, drive_id='me')

