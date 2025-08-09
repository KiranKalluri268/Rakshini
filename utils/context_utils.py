import json

LOG_FILE = "logs.json"


def log_event(event):
    # Load existing logs
    try:
        with open(LOG_FILE, 'r') as file:
            logs = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        logs = []

    # Append new event
    logs.append(event)

    # Save logs back to file
    with open(LOG_FILE, 'w') as file:
        json.dump(logs, file, indent=4)


def get_mocked_context():
    # Return mocked context data
    context = {
        "location": "MG Road",
        "time": "8:15 PM",
        "deviation": "User is not at home"
    }
    log_event({"action": "get_mocked_context", "context": context})
    return context

# Example usage
if __name__ == "__main__":
    context = get_mocked_context()
    print("Mocked Context:", context)
