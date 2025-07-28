from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window, StartMode
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Start
from aiogram_dialog.widgets.text import Const, Format
from cytoolz.itertoolz import getter

from cmd.getters.admin import get_users_count
from cmd.getters.user import get_user_balance
from cmd.handlers.admin import get_username, get_percent
from cmd.handlers.user import get_amount, get_wallet_and_memo
from cmd.states import AdminMenuSG, UserMenuSG

withdraw_dialog = Dialog(
    Window(
        Format("{BALANCE}"),
        Start(
            Const("💸 Withdraw Referral Balance"), id="withdraw_amount", state=UserMenuSG.WithdrawSG.enter_wallet),
        Start(Const("🔙 To main menu"), id="to_mein_panel", state=UserMenuSG.main_menu,
              mode=StartMode.RESET_STACK),
        state=UserMenuSG.WithdrawSG.withdraw_menu,
        getter=get_user_balance
    ),
    Window(
        Const("Enter Wallet address and memo(if there is):"),
        MessageInput(get_wallet_and_memo, content_types=[ContentType.TEXT]),
        Start(Const("🔙 To main menu"), id="to_mein_panel", state=UserMenuSG.main_menu,
              mode=StartMode.RESET_STACK),
        state=UserMenuSG.WithdrawSG.enter_wallet,
    ),
    Window(
        Const("Enter TON count:"),
        MessageInput(get_amount, content_types=[ContentType.TEXT]),
        Start(Const("🔙 To main menu"), id="to_mein_panel", state=UserMenuSG.main_menu,
              mode=StartMode.RESET_STACK),
        state=UserMenuSG.WithdrawSG.withdraw_amount,
    ),
    Window(
        Const("Your request has been received and sent to the admin. We will process your TON withdrawal within 24 hours."),
        Start(Const("🔙 To main menu"), id="to_mein_panel", state=UserMenuSG.main_menu,
              mode=StartMode.RESET_STACK),
        state=UserMenuSG.WithdrawSG.withdraw_final
    ),
)
