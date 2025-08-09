import requests

class SummarizerAgent:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = "https://api.gemini.com/v1/summarize"  # Example URL

    def send_to_llm(self, context):
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        data = {
            'context': context
        }
        response = requests.post(self.api_url, headers=headers, json=data)
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

    agent = SummarizerAgent(api_key)
    summary = agent.send_to_llm(context)
    print("Summary:", summary)

