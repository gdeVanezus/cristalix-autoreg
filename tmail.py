import requests
import re

base_url = "https://www.1secmail.com/api/v1/"

def get_temp_mail():
    new_mail_url = f"{base_url}?action=genRandomMailbox&count=1"

    try:
        response_new_mail = requests.get(new_mail_url)
        response_new_mail.raise_for_status()
        email = response_new_mail.json()
        email_address = email[0]

        return email_address
    

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None, None

def get_id(email):
    em = email.split('@')
    get_all_mail_url = f"{base_url}?action=getMessages&login={em[0]}&domain={em[1]}"

    try:
        response_all_mail = requests.get(get_all_mail_url)
        response_all_mail.raise_for_status()
        all_mail_data = response_all_mail.json()
        if all_mail_data:
            id_value = all_mail_data[0]['id']
            return id_value
        else:
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def get_cmail(email):
    em = email.split('@')
    get_all_mail_url = f"{base_url}?action=getMessages&login={em[0]}&domain={em[1]}"

    try:
        response_all_mail = requests.get(get_all_mail_url)
        response_all_mail.raise_for_status()

        all_mail_data = response_all_mail.json()
        
        id_value = all_mail_data[0]['id']
        
        return id_value

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def get_mail_url(email, mes_id):
    em = email.split('@')
    get_url = f"{base_url}?action=readMessage&login={em[0]}&domain={em[1]}&id={mes_id}"

    try:
        response_url = requests.get(get_url)
        response_url.raise_for_status()
        email_data = response_url.json()
        message_content = email_data['body']
        pattern = r'http://cristalix.gg/register/confirm/\?key=[^\'"]+'
        match = re.search(pattern, message_content)
        if match:
            return match.group(0)
        else:
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
