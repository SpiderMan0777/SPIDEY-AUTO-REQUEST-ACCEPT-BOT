# Don't Remove Credit @spideyofficial777
# Subscribe YouTube Channel For Amazing Bot @spidey_official_777
# Ask Doubt on telegram @hacker_x_official_777

import os
import asyncio
from aiofiles import os
import time
import logging
import random
from pyrogram import Client, filters, enums
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CallbackQuery,
)
from pyrogram.errors import (
    FloodWait,
    InputUserDeactivated,
    UserIsBlocked,
    UserNotParticipant,
    MessageTooLong,
    PeerIdInvalid,
)
from Spidey.database import get_all_users, add_user, already_db
from aiogram import Bot, Dispatcher, types
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Script import script
from leave import register_leave_handler
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pymongo.errors import PyMongoError
from configs import Spidey, temp


# Configuration do not remove otherwise bot will be crashed
API_ID = "28519661"
API_HASH = "d47c74c8a596fd3048955b322304109d"
BOT_TOKEN = ""
CHANNEL_IDS = [-1001959922658, -1002433552221, -1002470391435]
LOG_CHANNEL = -1002294764885
ADMINS = [5518489725]


# Image URLs
welcome_image_url = "https://i.ibb.co/CPxdkHR/IMG-20240818-192201-633.jpg"
background_image_url = "https://i.ibb.co/RymDMxS/66e7d1b6.jpg"
welcome_image = "https://envs.sh/v3t.jpg"

# Initialize the bot
app = Client("approver_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


# Approve join requests and send a welcome message
@app.on_chat_join_request(filters.group | filters.channel)
async def approve_join_request(_, message):
    try:
        await app.approve_chat_join_request(message.chat.id, message.from_user.id)

        chat = await app.get_chat(message.chat.id)
        channel_name = chat.title if chat.title else "our channel"

        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔔 Sᴜʙsᴄʀɪʙᴇ Tᴏ Oᴜʀ Cʜᴀɴɴᴇʟ",
                        url="https://youtube.com/@spidey_official_777",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Cᴏɴᴛᴀᴄᴛ Sᴜᴘᴘᴏʀᴛ", url="https://t.me/hacker_x_official_777"
                    )
                ],
            ]
        )
        await app.send_photo(
            message.from_user.id,
            background_image_url,
            caption=f"<b>Welcome {message.from_user.mention} to \n{channel_name}</b>",
            reply_markup=keyboard,
        )
    except Exception as err:
        print(f"Error approving join request: {str(err)}")


@app.on_message(filters.command("start"))
async def start(bot, message):
    try:
        if temp.U_NAME is None:
            temp.U_NAME = (await bot.get_me()).username
        if temp.B_NAME is None:
            temp.B_NAME = (await bot.get_me()).first_name  

    except Exception as e:
        print(f"Error sending reaction: {e}")  

    user_id = message.from_user.id
    user_name = message.from_user.first_name

    if not already_db(user_id):
        add_user(user_id, user_name)
                
        Spidey = (
            f"**#New_User {temp.B_NAME}**\n\n"
            f"≈ **ID:** `{user_id}`\n"
            f"≈ **Name:** {message.from_user.mention}\n"
            f"≈ **Username:** @{message.from_user.username if message.from_user.username else 'None'}\n"
            f"≈ **Group:** {message.chat.title if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP] else 'Private Chat'}"
        )
        await bot.send_message(LOG_CHANNEL, Spidey)

    try:        
        for channel in CHANNEL_IDS:
            try:
                await app.get_chat_member(channel, message.from_user.id)
            except UserNotParticipant:
                raise UserNotParticipant 

        if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
            buttons = [
                [InlineKeyboardButton('• ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴜʀ ᴄʜᴀᴛ •', url=f'http://t.me/{temp.U_NAME}?startgroup=true')],
                [
                    InlineKeyboardButton('• ᴍᴀsᴛᴇʀ •', url="https://t.me/hacker_x_official_777"),
                    InlineKeyboardButton('• sᴜᴘᴘᴏʀᴛ •', url='https://t.me/SPIDEYOFFICIAL_777')
                ],
                [InlineKeyboardButton('• ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ •', url="https://t.me/+9tdbATrOMLNlN2I1")]
            ]
            reply_markup = InlineKeyboardMarkup(buttons)
            await message.reply(script.GSTART_TXT.format(message.from_user.mention, temp.U_NAME, temp.B_NAME), reply_markup=reply_markup)
            return  

        if message.chat.type == enums.ChatType.PRIVATE:
            m = await message.reply_text("<b>ʜᴇʟʟᴏ ʙᴀʙʏ, ʜᴏᴡ ᴀʀᴇ ʏᴏᴜ \nᴡᴀɪᴛ ᴀ ᴍᴏᴍᴇɴᴛ ʙᴀʙʏ ....</b>")
            await asyncio.sleep(0.4)
            await m.edit_text("🎊")
            await asyncio.sleep(0.5)
            await m.edit_text("⚡")
            await asyncio.sleep(0.5)
            await m.edit_text("<b>ꜱᴛᴀʀᴛɪɴɢ ʙᴀʙʏ...</b>")
            await asyncio.sleep(0.4)
            await m.delete()

            m = await message.reply_sticker("CAACAgUAAxkBAAIdBGd7qZ7kMBTPT2YAAdnPRDtBSw9jwAACqwQAAr7vuFdHULNVi6H4nB4E")
            await asyncio.sleep(3)
            await m.delete()

            keyboard = InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("➕ Aᴅᴅ Mᴇ ᴛᴏ Yᴏᴜʀ Cʜᴀɴɴᴇʟ ➕", url="https://t.me/SPIDER_MAN_GAMING_bot?startchannel=Bots4Sale&admin=invite_users+manage_chat")],
                    [InlineKeyboardButton("🚀 Cʜᴀɴɴᴇʟ", url="https://t.me/+cMlrPqMjUwtmNTI1"),
                     InlineKeyboardButton("💬 Sᴜᴘᴘᴏʀᴛ", callback_data="group_info")],
                    [InlineKeyboardButton("ℹ️ Aʙᴏᴜᴛ", callback_data="about"),
                     InlineKeyboardButton("📃 Fᴇᴀᴛᴜʀᴇs", callback_data="features")],
                    [InlineKeyboardButton("➕  Aᴅᴅ Mᴇ ᴛᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ➕", url="https://t.me/SPIDER_MAN_GAMING_bot?startgroup=true")]
                ]
            )

            await message.reply_photo(
                photo=welcome_image_url,
                caption=(script.START_MSG.format(message.from_user.mention)),
                reply_markup=keyboard,
            )

    except UserNotParticipant:
        buttons = []
        for channel in CHANNEL_IDS:
            try:
                chat = await app.get_chat(channel)  
                if chat.username:
                    channel_link = f"https://t.me/{chat.username}"
                else:
                    channel_link = await app.export_chat_invite_link(channel) 

                buttons.append([InlineKeyboardButton(f"🚀 Join {chat.title}", url=channel_link)])

            except Exception as e:
                print(f"Error fetching channel link: {e}")  
                continue 

        buttons.append([InlineKeyboardButton("🔄 ᴄʜᴇᴄᴋ ᴀɢᴀɪɴ", callback_data="chk")])
        keyboard = InlineKeyboardMarkup(buttons)
        
        await message.reply_photo(
            photo=welcome_image,
            caption=f"<b>⚠️ Access Denied! ⚠️\n\n🔥 Hello {message.from_user.mention}!\n\n"
                    "You need to join all required channels before proceeding!\n\n"
                    "👉 [✨ Join Now ✨](https://t.me/SPIDEYOFFICIAL777)</b>",
            reply_markup=keyboard
        )



async def get_channel_link(client: Client, channel_id: int) -> str:
    """Fetches the invite link of a Telegram channel."""
    try:
        chat = await client.get_chat(channel_id)
        if chat.username:
            return f"https://t.me/{chat.username}"
        
        invite_link = chat.invite_link
        if not invite_link:
            invite_link = await client.export_chat_invite_link(channel_id)

        return invite_link  
    except Exception as e:
        print(f"Error fetching channel link: {e}")
        return "https://t.me/SPIDEYOFFICIAL777"  # Default backup link



@app.on_callback_query(filters.regex("chk"))
async def check_subscription(_, callback_query: CallbackQuery):
    try:
        for channel in CHANNEL_IDS:
            try:
                await app.get_chat_member(channel, callback_query.from_user.id)
            except UserNotParticipant:
                raise UserNotParticipant 
        keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("➕ Aᴅᴅ Mᴇ ᴛᴏ Yᴏᴜʀ Cʜᴀɴɴᴇʟ ➕", 
                    url="https://t.me/SPIDER_MAN_GAMING_bot?startchannel=Bots4Sale&admin=invite_users+manage_chat")],
                [InlineKeyboardButton("🚀 Cʜᴀɴɴᴇʟ", url="https://t.me/+cMlrPqMjUwtmNTI1"), 
                 InlineKeyboardButton("💬 Sᴜᴘᴘᴏʀᴛ", url="https://t.me/SPIDEYOFFICIAL777")],
                [InlineKeyboardButton("➕ Aᴅᴅ Mᴇ ᴛᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ➕", 
                    url="https://t.me/SPIDER_MAN_GAMING_bot?startgroup=true")]
            ]
        )

        await callback_query.message.edit_text(
            script.START_MSG.format(callback_query.from_user.mention),
            reply_markup=keyboard,
            disable_web_page_preview=True
        )

    except UserNotParticipant:
        buttons = []
        for channel in CHANNEL_IDS:
            try:
                chat = await app.get_chat(channel)  
                channel_name = chat.title if chat.title else "Channel"
                channel_link = f"https://t.me/{chat.username}" if chat.username else await app.export_chat_invite_link(channel)
                
                buttons.append([InlineKeyboardButton(f"🚀 Join {channel_name}", url=channel_link)])
            except Exception as e:
                print(f"Error fetching channel info: {e}")
                continue
        buttons.append([InlineKeyboardButton("🔄 ᴄʜᴇᴄᴋ ᴀɢᴀɪɴ", callback_data="chk")])
        keyboard = InlineKeyboardMarkup(buttons)     
        await callback_query.answer(
            "🙅 Yᴏᴜ ᴀʀᴇ ɴᴏᴛ sᴜʙsᴄʀɪʙᴇᴅ ᴛᴏ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ. Pʟᴇᴀsᴇ ᴊᴏɪɴ ᴀɴᴅ ᴄʟɪᴄᴋ 'Cʜᴇᴄᴋ Aɢᴀɪɴ' ᴛᴏ ᴄᴏɴғɪʀᴍ 🙅", 
            show_alert=True
        )
                            
                
@app.on_callback_query()
async def on_callback_query(_, callback_query: CallbackQuery):
    if callback_query.data == "features":
        await callback_query.message.edit_text(text="● ◌ ◌")
        await callback_query.message.edit_text(text="● ● ◌")
        await callback_query.message.edit_text(text="● ● ●")
        
        about_keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "sᴜʙsᴄʀɪʙᴇ", callback_data="feedback_feature"
                    ),
                    InlineKeyboardButton(
                        "ʀᴇᴍᴏᴠᴇʙɢ", url="https://example.com/removebg"
                    ),
                    InlineKeyboardButton(
                        "ʜᴀᴄᴋs", url="https://github.com/Spideyofficial777"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "Rɪɴɢᴛᴏɴᴇ", url="https://example.com/ringtone"
                    ),
                    InlineKeyboardButton("Cʜᴀᴛɢᴘᴛ", url="https://example.com/chatgpt"),
                    InlineKeyboardButton("Oᴡɴᴇʀ", callback_data="spidey"),
                ],
                [
                    InlineKeyboardButton("Mᴏᴠɪᴇs", url="https://example.com/movies"),
                    InlineKeyboardButton(
                        "Uᴘᴅᴀᴛᴇs", url="https://t.me/live_update_channel"
                    ),
                    InlineKeyboardButton(
                        "Sᴜᴘᴘᴏʀᴛ", url="https://t.me/SPIDEYOFFICIAL777"
                    ),
                ],
                [InlineKeyboardButton("⋞ Back", callback_data="back")],
            ]
        )

        await callback_query.message.edit_text(
            script.FEATURES_TXT, reply_markup=about_keyboard
        )

    elif callback_query.data == "about":
        await callback_query.message.edit_text(text="● ◌ ◌")
        await callback_query.message.edit_text(text="● ● ◌")
        await callback_query.message.edit_text(text="● ● ●")

        features_keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("‼️ ᴅɪꜱᴄʟᴀɪᴍᴇʀ ‼️", callback_data="disclaimer")],
                [
                    InlineKeyboardButton(
                        "• ᴠɪsɪᴛ ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ •", url="t.me/SPIDEYOFFICIAL_777"
                    )
                ],
                [
                    InlineKeyboardButton("• ᴏᴡɴᴇʀ •", user_id=int(7965267063)),
                    InlineKeyboardButton("• sᴏᴜʀᴄᴇ •", callback_data="source"),
                ],
                [InlineKeyboardButton("🛰️ ʀᴇɴᴅᴇʀɪɴɢ ꜱᴛᴀᴛᴜꜱ ☁️", callback_data="rendr")],
                [InlineKeyboardButton("⋞ Back ᴛᴏ ʜᴏᴍᴇ ", callback_data="back")],
            ]
        )

        await callback_query.message.edit_text(
            script.ABOUT_TXT, reply_markup=features_keyboard
        )

    elif callback_query.data == "feedback_feature":
        await callback_query.answer(
            "🛠️ Feedback: Save and display user feedback for admins seamlessly!",
            show_alert=True,
        )

    elif callback_query.data == "disclaimer":
        disclaimer_keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📲 ᴄᴏɴᴛᴀᴄᴛ ᴛᴏ ᴏᴡɴᴇʀ", url="https://t.me/hacker_x_official_777"
                    )
                ],
                [InlineKeyboardButton("⪻ ʙᴀᴄᴋ", callback_data="about")],
            ]
        )

        await callback_query.message.edit_text(text="● ◌ ◌")
        await callback_query.message.edit_text(text="● ● ◌")
        await callback_query.message.edit_text(text="● ● ●")

        await callback_query.message.edit_text(
            script.DISCLAIMER_TXT, reply_markup=disclaimer_keyboard
        )

    elif callback_query.data == "back":
        await callback_query.message.edit_text(text="● ◌ ◌")
        await callback_query.message.edit_text(text="● ● ◌")
        await callback_query.message.edit_text(text="● ● ●")

        welcome_message = script.START_MSG.format(callback_query.from_user.mention)

        main_keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                    "➕ Aᴅᴅ Mᴇ ᴛᴏ Yᴏᴜʀ Cʜᴀɴɴᴇʟ ➕",
                    url="https://t.me/SPIDER_MAN_GAMING_bot?startchannel=Bots4Sale&admin=invite_users+manage_chat",
                )
                ],
                [
                    InlineKeyboardButton("🚀 Channel", url="https://t.me/SPIDEYOFFICIAL_777"),
                    InlineKeyboardButton("💬 Sᴜᴘᴘᴏʀᴛ", callback_data="group_info"),
            ],
            [
                    InlineKeyboardButton("ℹ️ Aʙᴏᴜᴛ", callback_data="about"),
                InlineKeyboardButton("📃 Features", callback_data="features"),
                ],
                [
                    InlineKeyboardButton(
                    "➕ Aᴅᴅ Mᴇ ᴛᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ➕",
                    url="https://t.me/SPIDER_MAN_GAMING_bot?startgroup=true",
                )
            ],
        ]
    )

    # Final message
        await callback_query.message.edit_text(
        welcome_message,     reply_markup=main_keyboard
    )


    elif callback_query.data == "group_info":
        await callback_query.message.edit_text(text="● ◌ ◌")
        await callback_query.message.edit_text(text="● ● ◌")
        await callback_query.message.edit_text(text="● ● ●")

        buttons = [
            [
                InlineKeyboardButton(
                    "× ᴀʟʟ ᴏᴜʀ ʟɪɴᴋꜱ ×", url="https://t.me/SPIDEYOFFICIAL777"
                )
            ],
            [
                InlineKeyboardButton("• ɢʀᴏᴜᴘ •", url="https://t.me/+-eCz1o7dfZ0wMmI1"),
                InlineKeyboardButton(
                    "• ᴜᴘᴅᴀᴛᴇs •", url="https://t.me/+9tdbATrOMLNlN2I1"
                ),
            ],
            [
                InlineKeyboardButton("• ʜᴀᴄᴋ •", url="https://t.me/+cMlrPqMjUwtmNTI1"),
                InlineKeyboardButton(
                    "• ᴍᴏᴠɪᴇғʟɪx •", url="https://t.me/SPIDEYOFFICIAL_777"
                ),
            ],
            [
                InlineKeyboardButton(
                    "• ᴀɴɪᴍᴇ ᴄʀᴜɪsᴇ •", url="https://t.me/+4nyaulfn0sliZTE1"
                )
            ],
            [InlineKeyboardButton("⪻ ʙᴀᴄᴋ •", callback_data="back")],
        ]

        reply_markup = InlineKeyboardMarkup(buttons)

        await callback_query.message.edit_text(
            text=script.CHANNELS.format(callback_query.from_user.mention),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML,
        )

    elif callback_query.data == "rendr":
        await callback_query.answer(script.ALERT_MSG, show_alert=True)

    elif callback_query.data == "source":
        await callback_query.message.edit_text(text="● ◌ ◌")
        await callback_query.message.edit_text(text="● ● ◌")
        await callback_query.message.edit_text(text="● ● ●")

        buttons = [
        [
                InlineKeyboardButton("⪻ ʙᴀᴄᴋ", callback_data="about"),
                InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", callback_data="group_info"),
        ]
    ]

        reply_markup = InlineKeyboardMarkup(buttons)


        await callback_query.message.edit_text(
            text=script.SOURCE_TXT.format(
                callback_query.from_user.mention if callback_query.from_user else "User"
            ),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML,
            )



    elif callback_query.data == "spidey":
        await callback_query.message.edit_text(text="● ◌ ◌")
        await callback_query.message.edit_text(text="● ● ◌")
        await callback_query.message.edit_text(text="● ● ●")

        buttons = [
            [
                InlineKeyboardButton("⪻ ʙᴀᴄᴋ", callback_data="features"),
                InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", callback_data="group_info"),
        ]
    ]

        reply_markup = InlineKeyboardMarkup(buttons)

        await callback_query.message.edit_text(
            text=script.OWNER_TEXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML,
    )

@app.on_message(filters.command("users") & filters.user(ADMINS))
async def list_users(client, message: Message):
    Spidey = await message.reply("📌 **Fetching Users List...**")
    
    users_list = get_all_users()
    if not users_list:
        return await Spidey.edit_text("🚫 **No users found in the database.**")

    out = "👥 **Users Saved In DB:**\n\n"
    for user in users_list:
        user_id = user.get("user_id")
        user_name = user.get("name", f"User {user_id}")
        is_banned = user.get("ban_status", {}).get("is_banned", False)

        out += f"➤ <a href='tg://user?id={user_id}'>{user_name}</a>"
        if is_banned:
            out += " ❌ (Banned User)"
        out += "\n"

    await Spidey.edit_text(out)


@app.on_message(filters.command("broadcast") & filters.user(ADMINS) & filters.reply)
async def broadcast_users(bot, message):
    users = get_all_users()

    if not users:
        return await message.reply_text("🚫 **No users found in the database.**")

    broadcast_message = message.reply_to_message  
    Spidey = await message.reply_text("📡 **Broadcasting message to all users...**")
    
    total_users = len(list(users))
    success, failed = 0, 0
    start_time = time.time()

    
    for user in users:
        user_id = user.get("user_id")
        try:
            await bot.copy_message(
                chat_id=int(user_id),
                from_chat_id=broadcast_message.chat.id,
                message_id=broadcast_message.id
            )
            success += 1
        except UserIsBlocked:
            failed += 1
        except PeerIdInvalid:
            failed += 1
        except FloodWait as e:
            await asyncio.sleep(e.value)
        except Exception as e:
            print(f"Error broadcasting to {user_id}: {e}")
            failed += 1
        
        
        if (success + failed) % 10 == 0:
            await Spidey.edit_text(
                f"📡 **Broadcast in Progress...**\n\n"
                f"👥 **Total Users:** `{total_users}`\n"
                f"✅ **Successful:** `{success}`\n"
                f"❌ **Failed:** `{failed}`\n\n"
                f"🔥 **Powered by Spidey** 🕷️"
            )
    
    await Spidey.edit_text(
        f"📡 **Broadcast Completed!**\n\n"
        f"👥 **Total Users:** `{total_users}`\n"
        f"✅ **Successful:** `{success}`\n"
        f"❌ **Failed:** `{failed}`\n"
        f"🕒 **Time Taken:** `{round(time.time() - start_time, 2)} sec`\n\n"
        f"🚀 **Broadcast by [Spidey](https://t.me/SPIDEYOFFICIAL777)**\n"
        f"🔹 **Follow [Spidey Network](https://t.me/SPIDEY_CINEMA_X_AI_BOT)**"
    )
@app.on_message(filters.command("send") & filters.user(ADMINS))
async def send_msg(bot, message):
    if message.reply_to_message:
        target_ids = message.text.split(" ")[1:]
        if not target_ids:
            await message.reply_text("<b>ᴘʟᴇᴀꜱᴇ ᴘʀᴏᴠɪᴅᴇ ᴏɴᴇ ᴏʀ ᴍᴏʀᴇ ᴜꜱᴇʀ ɪᴅꜱ...</b>")
            return
        
        success_count = 0
        error_logs = ""

        try:
            for target_id in target_ids:
                try:
                    
                    if not already_db(target_id):
                        error_logs += f"❌ User ID <code>{target_id}</code> is not found in the database.\n"
                        continue
                    
                    user = await bot.get_users(target_id)
                    await message.reply_to_message.copy(int(user.id))
                    success_count += 1

                except Exception as e:
                    error_logs += f"‼️ Error in ID <code>{target_id}</code>: <code>{str(e)}</code>\n"

            # ✅ Ensure proper message formatting to avoid ENTITY_BOUNDS_INVALID error
            await message.reply_text(f"<b>✅ ꜱᴜᴄᴄᴇꜱꜱғᴜʟʟʏ ꜱᴇɴᴛ ᴍᴇꜱꜱᴀɢᴇꜱ ᴛᴏ `{success_count}` ᴜꜱᴇʀꜱ.\n\n{error_logs}</b>")

        except Exception as e:
            await message.reply_text(f"<b>‼️ Error - <code>{e}</code></b>")

    else:
        await message.reply_text("<b>ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴀꜱ ᴀ ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴍᴇꜱꜱᴀɢᴇ,\n"
                                 "ꜰᴏʀ ᴇɢ - <code>/send user_id1 user_id2</code></b>")

                                 

@app.on_message(filters.command("help"))
async def help_command(client, message):
    await message.reply_text(script.HELP_TXT)


if __name__ == "__main__":
    register_leave_handler(app)
    logging.basicConfig(level=logging.INFO)
    print(script.LOGO_MSG)
    app.run()


# Don't Remove Credit @spideyofficial777
# Subscribe YouTube Channel For Amazing Bot @spidey_official_777
# Ask Doubt on telegram @hacker_x_official_777
