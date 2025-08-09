import time

class FollowupAgent:
    def __init__(self, wait_time=30):
        self.wait_time = wait_time

    def wait_for_response(self):
        # Simulate waiting for a response
        print(f"Waiting for {self.wait_time} seconds for a response...")
        time.sleep(self.wait_time)

    def check_response(self, response_received):
        if response_received:
            print("Help is on the way.")
        else:
            print("No contact replied. Alerting nearest police or she-team...")

# Example usage
if __name__ == "__main__":
    agent = FollowupAgent()
    agent.wait_for_response()
    # Mocked response status
    response_received = False
    agent.check_response(response_received)
