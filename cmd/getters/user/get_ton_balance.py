from aiogram_dialog import DialogManager
from cmd.utils import UserAPI

async def get_user_balance(dialog_manager: DialogManager, **kwargs):
    api = UserAPI()
    # Получаем Telegram ID пользователя из update
    event = dialog_manager.event
    telegram_id = event.from_user.id if hasattr(event, "from_user") else None

    if not telegram_id:
        return {"BALANCE": "OPEN APP"}

    result = await api.create_user(telegram_id, "", "")
    if result and isinstance(result, dict):
        balance = result.get("balance_ton", 0)
        return {"BALANCE": f"Your balance: {balance} TON"}
    return {"BALANCE": "OPEN APP"}
