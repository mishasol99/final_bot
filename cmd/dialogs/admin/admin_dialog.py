from aiogram_dialog import Dialog, Window, StartMode
from aiogram_dialog.widgets.kbd import Start
from aiogram_dialog.widgets.text import Const

from cmd.states import AdminMenuSG

admin_dialog = Dialog(
    Window(
        Const("🔧 Адмін панель"),
        Start(Const("Підвищити відсоток рефералки"), id="up_referal_percent", state=AdminMenuSG.UpReferal.enter_name),
        Start(Const("Кол-во юзерів"), id="see_all_users", state=AdminMenuSG.SeeAllUsers.user_count),
        state=AdminMenuSG.admin_panel
    )
)
