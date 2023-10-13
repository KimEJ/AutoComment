# from bardapi import BardCookies
import asyncio
from sydney import SydneyClient
import os

class CreateComment:
    def __init__(self):
        pass
        # for cookie in cookies:
        #     if cookie['name'] == '_U':
        #         # self.cookies = cookie['value']
        #         print(cookie['value'])
        #         os.environ["BING_U_COOKIE"] = cookie['value']

    def create_comment(self, text):
        return asyncio.run(self.run(text))
    
    async def run(self, text):
        sydney = SydneyClient(style="creative")
        await sydney.start_conversation()
        response = await sydney.ask("다음 내용에 적절한 댓글을 200자 내로 작성해줘: "+text, citations=True)
        print(response)

        await sydney.close_conversation()
        return response