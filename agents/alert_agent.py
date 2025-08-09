class AlertAgent:
    def __init__(self, contacts):
        self.contacts = contacts

    def send_alert(self, summary):
        # Simulate sending the summary to emergency contacts
        for contact in self.contacts:
            print(f"Sending alert to {contact}: {summary}")

# Example usage
if __name__ == "__main__":
    # Mocked emergency contacts
    contacts = ["Contact 1", "Contact 2"]
    summary = "User Priya deviated from her usual safe zone at 8:15 PM and is currently at MG Road. She has confirmed she needs help."

    agent = AlertAgent(contacts)
    agent.send_alert(summary)
