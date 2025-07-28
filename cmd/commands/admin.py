import logging
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from cmd.states import AdminMenuSG

logger = logging.getLogger(__name__)

async def admin_start_cmd(message: Message, dialog_manager: DialogManager):
    admin_id = 544160143
    if message.from_user.id != admin_id:
        return
    await dialog_manager.start(AdminMenuSG.admin_panel)