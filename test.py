import asyncio

from PyPoeApi.poe_client import PoeClient, Chat

if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    PoeClient.ACCOUNT_FILE = r"account.yml"


    async def test():
        async with await PoeClient.create(playground_v2=True) as poe_client:
            chat = Chat()
            # 话题
            topics = await poe_client.ask(bot_name="Playground-v2",
                                          question="白天，下雨，沙滩，美女，长发，跳舞",
                                          chat=chat)
            print(topics)


    loop.run_until_complete(test())
