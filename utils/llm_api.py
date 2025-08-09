import requests

def send_to_llm(api_key, context):
    api_url = "https://api.gemini.com/v1/summarize"  # Example URL
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    data = {
        'context': context
    }
    response = requests.post(api_url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json().get('summary', 'No summary available')
    else:
        return f"Error: {response.status_code}"

# Example usage
if __name__ == "__main__":
    # Mocked API key and context
    api_key = "your_api_key_here"
    context = {
        "location": "MG Road",
        "time": "8:15 PM",
        "deviation": "User is not at home"
    }
    summary = send_to_llm(api_key, context)
    print("Summary:", summary)

