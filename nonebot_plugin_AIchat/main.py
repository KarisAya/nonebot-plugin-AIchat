import re
from nonebot import on_message
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from nonebot.typing import T_State
from abc import ABC, abstractmethod


class Basechat(ABC):
    @abstractmethod
    async def chat(self, nickname: str, content: str) -> str: ...


pattern = re.compile(r"[^\u4e00-\u9fa5a-zA-Z]")
str_filter = lambda x: pattern.sub("", x)


def create_chat(whitegroups: set[str], blackgroups: set[str], Chat: type[Basechat]) -> None:
    if whitegroups:
        check = lambda x: x in whitegroups
    elif blackgroups:
        check = lambda x: x not in blackgroups
    else:
        check = lambda x: True

    async def is_block(event: GroupMessageEvent, t_state: T_State) -> bool:
        group_id = str(event.group_id)
        if event.to_me and check(group_id):
            t_state["group_id"] = group_id
        else:
            return False
        return True

    chats: dict[str, Chat] = {}

    matcher = on_message(is_block, priority=200)

    @matcher.handle()
    async def _(event: GroupMessageEvent, t_state: T_State):
        group_id = t_state["group_id"]
        if group_id not in chats:
            chat = chats[group_id] = Chat()
        else:
            chat = chats[group_id]
        nickname = event.sender.card or event.sender.nickname
        await matcher.send(await chat.chat(nickname=str_filter(nickname), content=event.get_plaintext()))
        await matcher.finish()
