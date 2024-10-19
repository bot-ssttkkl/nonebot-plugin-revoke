from typing import Optional

from nonebot import on_command, logger
from nonebot.adapters.onebot.v11 import ActionFailed, Bot
from nonebot.internal.params import Depends
from nonebot.permission import SUPERUSER
from nonebot.plugin import PluginMetadata

from .utils import reply_message_id

__plugin_meta__ = PluginMetadata(
    name="主动消息撤回",
    description="让机器人撤回自己发出的消息",
    usage="向希望撤回的消息回复 /revoke",
    type="application",
    homepage="https://github.com/bot-ssttkkl/nonebot-plugin-revoke",
    supported_adapters={"~onebot.v11"}
)

revoke_matcher = on_command("revoke", aliases={"撤回"}, permission=SUPERUSER)


@revoke_matcher.handle()
async def _(
        bot: Bot,
        reply_msg_id: Optional[int] = Depends(reply_message_id)
):
    try:
        if reply_msg_id is not None:
            await bot.delete_msg(message_id=reply_msg_id)
    except ActionFailed as e:
        logger.exception(e)
