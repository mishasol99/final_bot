import asyncio
import logging
import aiohttp

from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardButton, WebAppInfo, InlineKeyboardMarkup, FSInputFile, Message
from aiogram_dialog import setup_dialogs, DialogManager

from cmd.commands import admin_start_cmd
from cmd.dialogs.admin import admin_dialog, users_count_dialog, up_referal_dialog
from cmd.dialogs.user import menu_dialog, withdraw_dialog
from cmd.states import UserMenuSG

router = Router()

@router.message(Command('start'))
async def command_start_handler(message: Message, dialog_manager: DialogManager):
    # Загружаем картинку
    # Извлекаем команду и реферальный ID
    start_command = message.text
    referrer_id = str(start_command[7:])

    if str(referrer_id) != "":
        if str(referrer_id) != str(message.from_user.id):
            async with aiohttp.ClientSession() as session:
                payload = {
                    "telegram_id": message.from_user.id,
                    "name": message.from_user.full_name,
                    "referrer_id": referrer_id
                }
                try:
                    async with session.post(
                            "https://buytelegramstarsapi-mishasoligan380.replit.app/api/v1/users/bot",
                            json=payload
                    ) as resp:
                        if resp.status == 200:
                            data = await resp.json()
                            print("✅ Успешно зарегистрирован:", data)
                        else:
                            print(f"❌ Ошибка регистрации: {resp.status}")
                except Exception as e:
                    print(f"⚠️ Ошибка соединения с сервером: {e}")
        await dialog_manager.start(UserMenuSG.main_menu)
    else:
        async with aiohttp.ClientSession() as session:
            payload = {
                "telegram_id": message.from_user.id,
                "name": message.from_user.full_name,
                "referrer_id": referrer_id
            }
            try:
                async with session.post(
                        "https://buytelegramstarsapi-mishasoligan380.replit.app/api/v1/users/bot",
                        json=payload
                ) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        print("✅ Успешно зарегистрирован:", data)
                    else:
                        print(f"❌ Ошибка регистрации: {resp.status}")
            except Exception as e:
                print(f"⚠️ Ошибка соединения с сервером: {e}")
        await dialog_manager.start(UserMenuSG.main_menu)


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(
        token="8385824657:AAFFqzV-bBOF5bCv0uKlv0Dv_pSUXwu4Sa4",
        default=DefaultBotProperties(parse_mode='HTML')
    )

    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    dp.include_router(router)
    setup_dialogs(dp)
    dp.message.register(admin_start_cmd, Command('admin'))

    # ADMIN DIALOGS
    dp.include_routers(admin_dialog, users_count_dialog, up_referal_dialog)

    # USER DIALOGS
    dp.include_routers(menu_dialog, withdraw_dialog)



    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
