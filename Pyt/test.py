import os  
import requests  
import base64  
from azure.identity import ClientSecretCredential  
  
# Configuration  
TENANT_ID = "YOUR_TENANT_ID"  
CLIENT_ID = "YOUR_CLIENT_ID"  
CLIENT_SECRET = "YOUR_CLIENT_SECRET"  
RESOURCE = "https://management.azure.com/.default"  
IMAGE_PATH = "YOUR_IMAGE_PATH"  
  
# Authenticate and get token  
credential = ClientSecretCredential(tenant_id=TENANT_ID, client_id=CLIENT_ID, client_secret=CLIENT_SECRET)  
token = credential.get_token(RESOURCE).token  
  
encoded_image = base64.b64encode(open(IMAGE_PATH, 'rb').read()).decode('ascii')  
  
headers = {  
    "Content-Type": "application/json",  
    "Authorization": f"Bearer {token}"  
}  
  
# Payload for the request  
payload = {
  "messages": [
    {
      "role": "system",
      "content": [
        {
          "type": "text",
          "text": "You are an AI assistant that helps people find information."
        }
      ]
    }
  ],
  "temperature": 0.7,
  "top_p": 0.95,
  "max_tokens": 800
}  
ENDPOINT = "https://zeuopenai-general.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-02-15-preview"  
  
# Send request  
try:  
    response = requests.post(ENDPOINT, headers=headers, json=payload)  
    response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code  
except requests.RequestException as e:  
    raise SystemExit(f"Failed to make the request. Error: {e}")  
  
# Handle the response as needed (e.g., print or process)  
print(response.json())