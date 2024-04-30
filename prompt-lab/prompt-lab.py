import requests

url = "https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29"

body = {
    "input": """I am thinking of travelling to Thailand. I like water sports and food. Give me 5 sentences on Thailand.
""",
    "parameters": {
        "decoding_method": "sample",
        "max_new_tokens": 200,
        "temperature": 0.7,
        "top_k": 50,
        "top_p": 1,
        "repetition_penalty": 1
    },
    "model_id": "meta-llama/llama-2-70b-chat",
    "project_id": "502a7e40-65e8-4a32-82d7-0c34b0dbc192",
    "moderations": {
        "hap": {
            "input": {
                "enabled": true,
                "threshold": 0.5,
                "mask": {
                    "remove_entity_value": true
                }
            },
            "output": {
                "enabled": true,
                "threshold": 0.5,
                "mask": {
                    "remove_entity_value": true
                }
            }
        }
    }
}

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_ACCESS_TOKEN"
}

response = requests.post(
    url,
    headers=headers,
    json=body
)

if response.status_code != 200:
    raise Exception("Non-200 response: " + str(response.text))

data = response.json()
