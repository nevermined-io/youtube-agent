# youtube_agent/__init__.py
import asyncio
from youtube_agent.main import main

def start():
    asyncio.run(main())