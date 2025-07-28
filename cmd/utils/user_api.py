import httpx
import logging

logger = logging.getLogger(__name__)

class UserAPI:
    def __init__(self, base_url: str = "https://buytelegramstarsapi-mishasoligan380.replit.app/api/v1"):
        self.base_url = base_url

    async def create_user(self, telegram_id: int, name: str, language: str):
        async with httpx.AsyncClient() as client:
            try:
                headers = {
                    "accept": "application/json",
                    "Content-Type": "application/json"
                }
                data = {
                    "telegram_id": telegram_id,
                    "name": name,
                    "language": language
                }
                response = await client.post(
                    f'{self.base_url}/users/',
                    headers=headers,
                    json=data,
                    timeout=10.0
                )
                if response.status_code == 200:
                    return response.json()
                logger.error(f'Failed to create user: {response.status_code} - {response.text}')
                return "Open APP"
            except httpx.RequestError as e:
                logger.error(f'Error creating user: {e}')
                return "Open APP"