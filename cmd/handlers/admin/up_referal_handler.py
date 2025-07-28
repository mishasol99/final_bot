from aiogram.types import Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput

from cmd.utils import AdminAPI


async def get_username(message: Message, message_input: MessageInput, dialog_manager: DialogManager):
    username = message.text
    dialog_manager.dialog_data['username'] = username
    await dialog_manager.next()

async def get_percent(message: Message, message_input: MessageInput, dialog_manager: DialogManager):
    api = AdminAPI()
    percent = message.text
    username = dialog_manager.dialog_data.get('username')
    result = await api.update_referral(username, percent)
    if result:
        await dialog_manager.next()
    else:
        await message.answer("Error")

