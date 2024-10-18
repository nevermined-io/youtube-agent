import os
import asyncio
from langchain.docstore.document import Document
from langchain_community.document_loaders import YoutubeLoader
from langchain_community.document_loaders.youtube import TranscriptFormat
from langchain_openai import OpenAI
from payments_py import Environment, Payments
from payments_py.data_models import AgentExecutionStatus
from langchain.chains.summarize import load_summarize_chain

nvm_api_key = os.getenv('NVM_API_KEY')
openai_api_key = os.getenv('OPENAI_API_KEY')
environment = os.getenv('ENVIRONMENT')


class YoutubeAgent:
    def __init__(self, payment):
        self.payment = payment

    async def run(self, data):
        print("Data received:", data)
        step = self.payment.ai_protocol.get_step(data['step_id'])


        loader = YoutubeLoader.from_youtube_url(
            youtube_url=step['input_query'],
            add_video_info=False, 
            language=["en"],
            transcript_format=TranscriptFormat.CHUNKS, 
            chunk_size_seconds=30,
        )
        # Load the documents from the video
        docs = loader.load()
        result = " ".join(doc.page_content for doc in docs)

        llm = OpenAI(api_key=openai_api_key)
        summarize_chain = load_summarize_chain(llm, chain_type="map_reduce")
        docs = [Document(page_content=result)]
        summary = summarize_chain.invoke(docs)
        print('Summary:', summary['output_text'])


        # Use the `payment` object to update the step
        self.payment.ai_protocol.update_step(
            did=data['did'],
            task_id=data['task_id'], 
            step_id=data['step_id'],
            step={'step_id': data['step_id'],
                    'task_id': data["task_id"], 
                    'step_status': AgentExecutionStatus.Completed.value,
                    'output': summary['output_text'],
                    'is_last': True
                    },
        )

async def main():
    # Initialize the Payments object
    payment = Payments(
        app_id="youtube_agent", 
        nvm_api_key=nvm_api_key, 
        version="1.0.0", 
        environment=Environment.appStaging, 
        ai_protocol=True, 
        web_socket_options={'bearer_token': nvm_api_key}
    )

    # Initialize the YoutubeAgent with the payment instance
    agent = YoutubeAgent(payment)

    # Subscribe to the ai_protocol with the agent's `run` method
    subscription_task = asyncio.get_event_loop().create_task(payment.ai_protocol.subscribe(agent.run, join_account_room=True))
    try:
        await subscription_task
    except asyncio.CancelledError:
        print("Subscription task was cancelled")

