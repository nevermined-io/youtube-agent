# YouTube Agent

The Youtube Summarizer it's a small Python AI Agent with Nevermined Payments Library integrated which receives a Youtube video URL and returns a summary of the transcription of the video.
The Agent uses LangChain to retrieve the transcription and summarize it via OpenAI integration. 


## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/nevermined-io/youtube-agent.git
    cd youtube-agent
    ```

2. Install dependencies:
    ```bash
    poetry shell
    poetry install
    ```

3. Set up environment variables:
    Create a `.env` file in the root directory and add your env variables:
    ```env
    NVM_API_KEY='ey...'
    OPENAI_API_KEY='sh-...'
    NVM_ENVIRONMENT='testing'
    AGENT_DID='did:nv:...'
    ```

## Usage

1. Start the application:
    ```bash
    poetry run start
    ```

## main.py

The `main.py` script is the entry point for the YouTube Agent. As you can see, the Agent is a simple Python script that implements a callback function to process the AI Tasks that are sent by the users.

## two_steps_main.py

The `two_steps_main.py` script is the entry point for the YouTube Agent. As you can see, the Agent is a simple Python script that implements a callback function to process the AI Tasks that are sent by the users. This script is used to demonstrate the two-step process of the AI Task execution with the Nevermined SDK that is recommended to handled task that require a long time to be processed.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

