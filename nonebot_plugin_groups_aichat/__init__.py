from nonebot import get_driver, on_message, get_plugin_config
from nonebot.adapters.onebot.v11 import Bot, MessageEvent
from nonebot.plugin import PluginMetadata
from clovers import Leaf
from clovers.config import Config as CloversConfig
from .config import Config

# nonebot_plugin_clovers 内配置了 clovers 的 logger 所以需要先导入。

from nonebot_plugin_clovers.adapters.onebot.v11 import __adapter__ as adapter

# 先注入配置，再加载插件。
# 因为模块导入机制，如果 clovers_AIchat 被导入过则此配置会失效。

clovers_config = CloversConfig.environ()

clovers_config["clovers_AIchat"] = {k[29:]: v for k, v in get_plugin_config(Config).model_dump().items()}

from clovers_AIchat import __plugin__ as plugin

__plugin_meta__ = PluginMetadata(
    name="AI群聊机器人",
    description="AI群聊机器人",
    usage="@BOT 聊天内容",
    type="application",
    config=Config,
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


clovers_config.save()
