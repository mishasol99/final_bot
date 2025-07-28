from aiogram_dialog import Dialog, Window, StartMode
from aiogram_dialog.widgets.kbd import Start
from aiogram_dialog.widgets.text import Const, Format

from cmd.getters.admin import get_users_count
from cmd.states import AdminMenuSG

users_count_dialog = Dialog(
    Window(
        Format("{USERS_COUNT}"),
        Start(Const("Назад"), id="to_main_menu", state=AdminMenuSG.admin_panel),
        state=AdminMenuSG.SeeAllUsers.user_count,
        getter=get_users_count
    )
)
