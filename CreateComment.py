# from bardapi import BardCookies
import asyncio
from sydney import SydneyClient
import aiohttp
import os

class CreateComment:
    def __init__(self, token):
        # pass
        self.loop = asyncio.get_event_loop()
        self.session = self.get_session(token)
        self.room = None

    def get_session(self, token):
        session = aiohttp.ClientSession(headers={"Authorization": "Bearer "+token})
        return session

    async def create_chat(self):
        if(self.room):
            await self.delete_chat(self.room)
            self.room = None

        async with self.session.post(f'https://api.wow.wrtn.ai/chat') as request:
            response = await request.json()
            print(response)
            result = response['result']
            if result != "SUCCESS":
                raise Exception("Failed to create chat session")

            self.room = response['data']['_id']

            return self.room
    
    async def delete_chat(self, room):
        room = room or self.room
        async with self.session.delete(f'https://api.wow.wrtn.ai/chat/{room}') as request:
            response = await request.json()
            print(response)
            return response
        
    async def chat(self, text):
        async with self.session.post(f'https://william.wow.wrtn.ai/chat/{self.room}', json={"message": text, "reroll": False}) as request:
            print('run')
            response = await request.json()
            if response['result'] != "SUCCESS":
                raise Exception("Failed to send chat")
            
            print(response['data']['content'])
            return response['data']['content']