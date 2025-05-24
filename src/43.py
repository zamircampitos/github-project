import os
import requests

def send_email(email):
    # Replace 'your_email' with your actual email address and make sure to replace 'password' with your actual password
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.environ['SALT']}"
    }
    data = {"to": email, "subject": "Test Email", "body": "This is a test email sent from GitHub"}
    response = requests.post("https://api.github.com/repos/your-repo-name/issues/1947", headers=headers, json=data)
    if response.status_code == 201:
        print(f"Email {email} has been created. Message ID: {response.json()['message_id']}")
    else:
        print(f"Failed to create the email. Status code: {response.status_code}")

# Example usage
send_email("example@example.com")
