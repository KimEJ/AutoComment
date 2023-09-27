# from bardapi import BardCookies
from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle
import asyncio

class CreateComment:
    def __init__(self, cookies):
        self.cookies = cookies
        # self.bing = asyncio.run(Chatbot.create(cookies=cookies))
        # print(self.bing.ask(prompt="다음 내용에 적절한 댓글을 200자 내로 작성해줘"))

        # 비동기로 요청 보낸 후 넘어가기
        # asyncio.run(self.run("다음 내용에 적절한 댓글을 200자 내로 작성해줘"))

        # print("bard init")
        
        # session = requests.Session()
        # token = "bard __Secure-1PSID token"
        # session.cookies.set("__Secure-1PSID", "bard __Secure-1PSID token")
        # session.cookies.set( "__Secure-1PSIDCC", "bard __Secure-1PSIDCC token")
        # session.cookies.set("__Secure-1PSIDTS", "bard __Secure-1PSIDTS token")
        # session.headers = SESSION_HEADERS

        # bard = Bard(token=token, session=session)
        # self.bard = Bard(token_from_browser=True)
        
    #     cookie_dict = {}
    #     for cookie in cookies:
    #         cookie_dict[cookie["name"]] = cookie["value"]

    #     self.bard = BardCookies(cookie_dict=cookie_dict)
    #     # print(self.bard.get_answer("다음 내용에 적절한 댓글을 200자 내로 작성해줘")["content"])

    def create_comment(self, text):
        return asyncio.run(self.run(text))
    #     return self.bard.get_answer("다음 내용에 적절한 댓글을 200자 내로 작성해줘: \n"+text)["content"]
    
    async def run(self, text):
        bing = await Chatbot.create(cookies=self.cookies)
        # self.run("다음 내용에 적절한 댓글을 200자 내로 작성해줘")
        response = await bing.ask(prompt="다음 내용에 적절한 댓글을 200자 내로 작성해줘: "+text, conversation_style=ConversationStyle.creative)
        # print(response)
        response = response['item']['messages']
        comment = ""
        for message in response:
            if message['author'] == 'bot':
                comment += message['text'] + "\n"

        await bing.close()
        return comment