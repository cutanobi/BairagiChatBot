from pyrogram import filters
from pyrogram.types import Message

from Asuraa import OWNER, dev
from Asuraa.database.chats import get_served_chats
from Asuraa.database.users import get_served_users


@dev.on_message(filters.command("stats") & filters.user(OWNER))
async def stats(cli: dev, message: Message):
    users = len(await get_served_users())
    chats = len(await get_served_chats())
    await message.reply_text(
        f"""ᴀʟʟ sᴛᴀᴛs ᴏғ ᴍᴀʜᴀᴋ ᴄʜᴀᴛʙᴏᴛ {(await cli.get_me()).mention} :

๏ **ᴄʜᴀᴛs ➛** {chats}
๏ **ᴜsᴇʀs ➛** {users}"""
    )
