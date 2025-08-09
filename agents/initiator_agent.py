class InitiatorAgent:
    def __init__(self):
        # Mocked context data
        self.current_location = "MG Road"
        self.expected_location = "Home"
        self.current_time = "8:15 PM"

    def check_context(self):
        # Check if the user is at the expected location
        if self.current_location != self.expected_location:
            return True
        return False

    def display_prompt(self):
        # Display a prompt to the user
        if self.check_context():
            print("You usually stay home at 8PM. You are currently near MG Road. Do you need help?")
            print("[Yes] [No]")

# Example usage
if __name__ == "__main__":
    agent = InitiatorAgent()
    agent.display_prompt()

