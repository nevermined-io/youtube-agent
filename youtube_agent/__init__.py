# youtube_agent/__init__.py
import asyncio
from youtube_agent.main import main
from youtube_agent.two_steps_main import two_steps_main


def start():
    asyncio.run(main())


def start_two_steps_main():
    asyncio.run(two_steps_main())
