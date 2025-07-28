from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window, StartMode
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Start
from aiogram_dialog.widgets.text import Const, Format

from cmd.getters.admin import get_users_count
from cmd.handlers.admin import get_username, get_percent
from cmd.states import AdminMenuSG

up_referal_dialog = Dialog(
    Window(
        Const("Ваедите юзернейм:"),
        MessageInput(get_username, content_types=[ContentType.TEXT]),
        state=AdminMenuSG.UpReferal.enter_name
    ),
    Window(
        Const("Ваедите кол-во процентів:"),
        MessageInput(get_percent, content_types=[ContentType.TEXT]),
        state=AdminMenuSG.UpReferal.enter_percent,
    ),
    Window(
        Const("Кол-во процентів успішно змінено:"),
        Start(Const("В головне меню"), id="to_mein_panel", state=AdminMenuSG.admin_panel,
              mode=StartMode.RESET_STACK),
        state=AdminMenuSG.UpReferal.up_referal_final
    ),
)
