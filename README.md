<div align="center">

<a href="https://v2.nonebot.dev/store">
  <img src="https://raw.githubusercontent.com/A-kirami/nonebot-plugin-template/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo">
</a>

<p>
  <img src="https://raw.githubusercontent.com/A-kirami/nonebot-plugin-template/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText">
</p>

# nonebot-plugin-groups-aichat

AI 群聊机器人群聊

[![python](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/)
[![license](https://img.shields.io/github/license/KarisAya/nonebot_plugin_groups_aichat.svg)](./LICENSE)
[![pypi](https://img.shields.io/pypi/v/nonebot_plugin_groups_aichat.svg)](https://pypi.python.org/pypi/nonebot_plugin_groups_aichat)
[![pypi download](https://img.shields.io/pypi/dm/nonebot_plugin_groups_aichat)](https://pypi.python.org/pypi/nonebot_plugin_groups_aichat)
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)

</div>

# 配置

具体配置方法请参考 [clovers-AIchat](https://github.com/clovers-project/clovers-AIchat)

```env
NONEBOT_PLUGIN_GROUPS_AICHAT_TIMEOUT = 600
NONEBOT_PLUGIN_GROUPS_AICHAT_MEMORY = 20
NONEBOT_PLUGIN_GROUPS_AICHAT_PROMPT_SYSTEM = '你的名字是枫枫，你可以自由回答问题。'
NONEBOT_PLUGIN_GROUPS_AICHAT_CONFIG_LIST = '
[
	{
		"key": "hunyuan",
		"model": "hunyuan-lite",
		"url": "https://hunyuan.tencentcloudapi.com",
		"secret_id": "",
		"secret_key": ""
	}
]
'
```

# 💿 安装

<details open>
<summary>[推荐] 使用 nb-cli 安装</summary>

在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

```bash
nb plugin install nonebot_plugin_groups_aichat
```

</details>

<details>
<summary>使用包管理工具</summary>

使用 poetry/pip 等包管理工具在当前目录安装本插件

之后打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分的 `plugins` 项里追加写入

```toml
[tool.nonebot]
plugins = [
    # ...
    "nonebot_plugin_groups_aichat"
]
```

</details>

</div>

# 📞 联系

如有建议，bug 反馈等可以加群

机器人 bug 研究中心（闲聊群） 744751179

永恒之城（测试群） 724024810

![群号](https://github.com/KarisAya/clovers/blob/master/%E9%99%84%E4%BB%B6/qrcode_1676538742221.jpg)
