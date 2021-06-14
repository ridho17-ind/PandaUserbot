from telethon.tl.functions.contacts import UnblockRequest
from telethon.errors.rpcerrorlist import YouBlockedUserError
from Panda import pandaub

plugin_category = "utils"

chat = "@BotFather"

@pandaub.ilhammansiz_cmd(
    pattern="botfather(?: |$)(.*)",
    command=("botfather", plugin_category),
    info={
        "header": "Membuat bot di bot father.",
        "description": "Membuat bot di bot father.",
        "usage": "{tr}botfather <namabot> <usernamebot",
        ],
        "examples": [
            "{tr}botfather <namabot> <usernamebot>",
        ],
    },
)
async def _(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        text, username = event.pattern_match.group(1).split()

    else:
        await event.edit("`Masukan Yang Benar Cok Biar Bisa Bikin Bot!!`")
        return

    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("/newbot")
            audio = await conv.get_response()
            await conv.send_message(text)
            audio = await conv.get_response()
            await conv.send_message(username)
            audio = await conv.get_response()
            await event.client.forward_messages(event.chat_id, audio)
            await event.delete()
        except YouBlockedUserError:
            await event.client(UnblockRequest("93372553"))
            await conv.send_message("/newbot")
            audio = await conv.get_response()
            await conv.send_message(text)
            audio = await conv.get_response()
            await conv.send_message(username)
            audio = await conv.get_response()
            await event.client.forward_messages(event.chat_id, audio)
            await event.delete()

