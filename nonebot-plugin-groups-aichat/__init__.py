from nonebot import get_driver, on_message
from nonebot.adapters.onebot.v11 import Bot, MessageEvent
from nonebot.plugin import PluginMetadata
from clovers import Leaf
from nonebot_plugin_clovers.adapters.onebot.v11 import __adapter__ as adapter
from clovers_AIchat import __plugin__ as plugin
from nonebot.plugin import PluginMetadata

__plugin_meta__ = PluginMetadata(
    name="AI群聊机器人群聊",
    description="AI群聊机器人群聊",
    usage="@BOT 聊天内容",
    type="application",
    homepage="https://github.com/KarisAya/nonebot_plugin_groups_aichat",
    supported_adapters={"nonebot.adapters.onebot.v11"},
)

leaf = Leaf(adapter)
leaf.plugins.append(plugin)
driver = get_driver()
driver.on_startup(leaf.startup)
driver.on_shutdown(leaf.shutdown)

main = on_message(priority=100, block=True)


@main.handle()
async def _(bot: Bot, event: MessageEvent):
    leaf.response(event.get_plaintext(), bot=bot, event=event)
