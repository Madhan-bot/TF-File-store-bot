import base64
import re
import asyncio
from pyrogram import filters
from pyrogram.enums import ChatMemberStatus
from config import FORCE_SUB_CHANNEL_1, FORCE_SUB_CHANNEL_2, FORCE_SUB_CHANNEL_3, FORCE_SUB_CHANNEL_4, ADMINS
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram.errors import FloodWait

# --- FIX 1: Use a raw string (r"") for regex to fix SyntaxWarning ---
async def get_message_id(client, message):
    if message.forward_from_chat:
        if message.forward_from_chat.id == client.db_channel.id:
            return message.forward_from_message_id
        else:
            return 0
    elif message.forward_sender_name:
        return 0
    elif message.text:
        # Added 'r' before the quotes
        pattern = r"https://t.me/(?:c/)?(.*)/(\d+)"
        matches = re.match(pattern, message.text)
        if not matches:
            return 0
        channel_id = matches.group(1)
        msg_id = int(matches.group(2))
        if channel_id.isdigit():
            if f"-100{channel_id}" == str(client.db_channel.id):
                return msg_id
        else:
            if channel_id == client.db_channel.username:
                return msg_id
    else:
        return 0

# --- FIX 2: Optimized Subscription Check ---
async def check_subscribe(client, chat_id, user_id):
    if not chat_id:
        return True
    if user_id in ADMINS:
        return True
    try:
        member = await client.get_chat_member(chat_id=chat_id, user_id=user_id)
    except UserNotParticipant:
        return False
    except Exception:
        # If there's a CHANNEL_INVALID error, it returns False or you can log it
        return False

    return member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.MEMBER]

# Updated filters using the optimized function
subscribed1 = filters.create(lambda _, c, u: check_subscribe(c, FORCE_SUB_CHANNEL_1, u.from_user.id))
subscribed2 = filters.create(lambda _, c, u: check_subscribe(c, FORCE_SUB_CHANNEL_2, u.from_user.id))
subscribed3 = filters.create(lambda _, c, u: check_subscribe(c, FORCE_SUB_CHANNEL_3, u.from_user.id))
subscribed4 = filters.create(lambda _, c, u: check_subscribe(c, FORCE_SUB_CHANNEL_4, u.from_user.id))
