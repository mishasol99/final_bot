from aiogram.fsm.state import StatesGroup, State

class AdminMenuSG(StatesGroup):
    admin_panel = State()

    class UpReferal(StatesGroup):
        enter_name = State()
        enter_percent = State()
        up_referal_final = State()

    class SeeAllUsers(StatesGroup):
        user_count = State()

