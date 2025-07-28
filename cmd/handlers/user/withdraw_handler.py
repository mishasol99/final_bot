from aiogram import types
from aiogram.types import Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput
from cmd.utils import UserAPI

async def get_wallet_and_memo(message: Message, message_input: MessageInput, dialog_manager: DialogManager):
    wallet_and_memo = message.text
    dialog_manager.dialog_data['wallet_and_memo'] = wallet_and_memo
    await dialog_manager.next()

async def get_amount(message: Message, message_input: MessageInput, dialog_manager: DialogManager):
    amount = float(message.text)
    dialog_manager.dialog_data['amount'] = amount
    wallet_and_memo = dialog_manager.dialog_data.get('wallet_and_memo')
    api = UserAPI()
    telegram_id = message.from_user.id
    result = await api.create_user(telegram_id, "", "")
    if result and isinstance(result, dict):
        balance = result.get("balance_ton", 0)
        if amount >= 1:
            if balance >= amount:
                admin_message = f"Withdrawal request:\nID: {telegram_id}\nAmount: {amount} TON\nWallet amd memo: {wallet_and_memo}"

                # Получаем бота через middleware_data
                bot = dialog_manager.middleware_data["bot"]

                await bot.send_message(544160143, admin_message)
                await dialog_manager.next()
        else:
            await message.answer("Insufficient balance for withdrawal.")


