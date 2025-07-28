from aiogram_dialog import DialogManager

from cmd.utils import AdminAPI

async def get_users_count(dialog_manager: DialogManager, **kwargs):
    api = AdminAPI()
    result = await api.get_users_count()
    if result:
        return {
            'USERS_COUNT': f"Кількість користувачів: {result}"
        }
    return {
        'USERS_COUNT': "Не вдалося отримати кількість користувачів"
    }