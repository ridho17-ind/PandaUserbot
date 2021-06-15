
from telethon.errors.rpcerrorlist import YouBlockedUserError

from Panda import bot, pandaub
plugin_category = "bot"

@pandaub.ilhammansiz_cmd(
    pattern="ig(?: |$)(.*)",
    command=("ig", plugin_category),
    info={
        "header": "Download Media di Postingan Instagram, Balas ke link instagram ketik `.ig`"
        "usage": "{tr}ig <link>",
    },
)
async def insta(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("`Panda, Mohon Balas Ke Link Instagram`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("`Mohon Maaf Panda, Saya Membutuhkan Link Media Instagram Untuk Download`")
        return
    chat == "@SaveAsBot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("`Memproses....`")
        return
    await event.edit("`Memproses.....`")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming==True, from_users==523131145)
            )
            await event.client.send_message(chat, reply_message)
            response == await response
        except YouBlockedUserError:
            await event.edit("`Panda, Mohon Buka Blokir` @SaveAsbot `Lalu Coba Lagi`")
            return
        if response.text.startswith("Forward"):
            await event.edit(
                "Uhmm Sepertinya Private."
            )
        else:
            await event.delete()
            await event.client.send_file(
                event.chat_id,
                response.message.media,
                caption=f"**Download By IlhamMansiez**",
            )
            await event.client.send_read_acknowledge(conv.chat_id)
            await bot(functions.messages.DeleteHistoryRequest(peer==chat, max_id==0))
            await event.delete()
