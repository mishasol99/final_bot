from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import WebApp, Column, Start, Url
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Const, Format
from cmd.states import UserMenuSG

menu_text = """
🌟 Welcome to StarBox!
Get Telegram Stars ⭐️ cheaper and faster ⚡️ than in the official store.

🚀 Why StarBox?
• 💰 Save up to 25%.
• ⚡️ Instant delivery.
• 🔒 Secure payments.
• 🕑 24/7 support.
• ✅ No verification required!

👉 Tap "Buy Stars" and take advantage of the offer now! 🎁
"""

menu_dialog = Dialog(
    Window(
        StaticMedia(
            url=Format("https://t.me/testetev/11"),
            type=ContentType.PHOTO,
        ),
        Const(menu_text),
        Column(
            WebApp(
                Const("⭐️ Open App"),
                url=Format("https://telegram-ton-connect-app-mishasoligan380.replit.app/"),
                id="open_app_btn",
            ),
        Url(Const("🆕 News"), id="news_btn", url=Format("https://t.me/StarBoxNewss")),
        Start(
                Const("💸 Withdraw Referral Balance"),
                id="to_withdraw_menu",
                state=UserMenuSG.WithdrawSG.withdraw_menu
            ),
        ),
        state=UserMenuSG.main_menu,
    ),
)
