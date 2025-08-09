## Rakshini-An Agentic AI Companion for Women’s Safety

## Overview
The Rakshini project is designed to enhance safety measures by utilizing various agents that work together to monitor, alert, and respond to potential safety threats. This project leverages AI and context-aware systems to provide timely alerts and follow-ups.

## Project Structure

- **agents/**: Contains the different agents responsible for various tasks.
  - `alert_agent.py`: Manages alert notifications to predefined contacts.
  - `followup_agent.py`: Handles follow-up actions and checks for responses.
  - `initiator_agent.py`: Initiates the process by checking context and displaying prompts.
  - `summarizer_agent.py`: Summarizes context and interacts with language models.
  - `trigger_agent.py`: Captures context and triggers necessary actions based on location, time, and deviation.

- **utils/**: Utility scripts to support the main agents.
  - `context_utils.py`: Provides functions to log events and retrieve mocked contexts.
  - `llm_api.py`: Interfaces with language models using API keys.

- **app.py**: The main application script that orchestrates the interaction between different agents and utilities.

## Getting Started

1. **Installation**: Ensure you have Python installed. Clone the repository and install necessary dependencies.
   ```bash
   git clone <repository-url>
   cd women-safety-demo
   pip install -r requirements.txt
   ```

2. **Configuration**: Set up your environment variables and API keys as needed.

3. **Running the Application**: Execute the main application script.
   ```bash
   python app.py
   ```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact
For any inquiries or support, please contact at [kirankalluri888@gmail.com].
