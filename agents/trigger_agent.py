class TriggerAgent:
    def __init__(self, location, time, deviation):
        self.location = location
        self.time = time
        self.deviation = deviation

    def capture_context(self):
        # Capture the context details
        context = {
            "location": self.location,
            "time": self.time,
            "deviation": self.deviation
        }
        return context

    def trigger_chain(self, context):
        # Trigger the next agent in the chain
        print("Triggering agent chain with context:", context)

# Example usage
if __name__ == "__main__":
    # Mocked context data
    location = "MG Road"
    time = "8:15 PM"
    deviation = "User is not at home"

    agent = TriggerAgent(location, time, deviation)
    context = agent.capture_context()
    agent.trigger_chain(context)

