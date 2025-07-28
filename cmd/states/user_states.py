from aiogram.fsm.state import StatesGroup, State

class UserMenuSG(StatesGroup):
    main_menu = State()

    class WithdrawSG(StatesGroup):
        withdraw_menu = State()
        enter_wallet = State()
        withdraw_amount = State()
        withdraw_final = State()
