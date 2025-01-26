from nonebot import get_driver, on_message, get_plugin_config
from nonebot.adapters.onebot.v11 import Bot, MessageEvent
from nonebot.plugin import PluginMetadata
from clovers import Leaf
from clovers.config import config as clovers_config
from .config import Config

# 先注入配置，再加载插件。
# 因为模块导入机制，如果 clovers_AIchat 被导入过则此配置会失效。

clovers_config["clovers_AIchat"] = {k.lstrip("nonebot_plugin_groups_aichat_"): v for k, v in get_plugin_config(Config).model_dump().items()}

from clovers_AIchat import __plugin__ as plugin
from nonebot_plugin_clovers.adapters.onebot.v11 import __adapter__ as adapter


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


@on_message(priority=100, block=True).handle()
async def _(bot: Bot, event: MessageEvent):
    await leaf.response(event.get_plaintext(), bot=bot, event=event)
