import streamlit as st
from agents.initiator_agent import InitiatorAgent
from agents.trigger_agent import TriggerAgent
from agents.summarizer_agent import SummarizerAgent
from agents.alert_agent import AlertAgent
from agents.followup_agent import FollowupAgent
from utils.context_utils import get_mocked_context, log_event
from utils.llm_api import send_to_llm

# Initialize agents
initiator_agent = InitiatorAgent()
context = get_mocked_context()
log_event({"action": "initialize_agents", "context": context})

# Streamlit UI
st.title("Agentic AI Companion for Women’s Safety")

# Initiator Agent
if initiator_agent.check_context():
    st.write("You usually stay home at 8PM. You are currently near MG Road. Do you need help?")
    if st.button("Yes"):
        log_event({"action": "user_response", "response": "Yes"})
        # Trigger Agent
        trigger_agent = TriggerAgent(context['location'], context['time'], context['deviation'])
        captured_context = trigger_agent.capture_context()
        log_event({"action": "capture_context", "captured_context": captured_context})
        
        # Summarizer Agent
        api_key = "your_api_key_here"  # Replace with actual API key
        summarizer_agent = SummarizerAgent(api_key)
        summary = summarizer_agent.send_to_llm(captured_context)
        st.write("Summary:", summary)
        log_event({"action": "summarize_context", "summary": summary})

        # Alert Agent
        contacts = ["Contact 1", "Contact 2"]
        alert_agent = AlertAgent(contacts)
        alert_agent.send_alert(summary)
        log_event({"action": "send_alert", "summary": summary, "contacts": contacts})

        # Follow-up Agent
        followup_agent = FollowupAgent()
        followup_agent.wait_for_response()
        # Mocked response status
        response_received = False
        followup_agent.check_response(response_received)
        log_event({"action": "check_response", "response_received": response_received})
    elif st.button("No"):
        st.write("Stay safe!")
        log_event({"action": "user_response", "response": "No"})
