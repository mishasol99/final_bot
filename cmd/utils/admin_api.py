import httpx
import logging

logger = logging.getLogger(__name__)

class AdminAPI:
    def __init__(self, base_url: str = "https://buytelegramstarsapi-mishasoligan380.replit.app/api/v1"):
        self.base_url = base_url

    async def update_referral(self, name: str, percent: int):
        async with httpx.AsyncClient() as client:
            try:
                headers = {
                    "accept": "application/json",
                    "Content-Type": "application/json"
                }
                data = {
                    "name": name,
                    "percent": percent
                }
                response = await client.post(
                    f'{self.base_url}/users/up_referal',
                    headers=headers,
                    json=data,
                    timeout=10.0
                )
                if response.status_code == 200:
                    return response.json()
                logger.error(f'Failed to update referral: {response.status_code} - {response.text}')
                return None
            except httpx.RequestError as e:
                logger.error(f'Error updating referral: {e}')
                return None


    async def get_users_count(self):
        async with httpx.AsyncClient() as client:
            try:
                headers = {"accept": "application/json"}
                response = await client.get(
                    f'{self.base_url}/users/count',
                    headers=headers,
                    timeout=10.0
                )
                if response.status_code == 200:
                    return response.json()
                logger.error(f'Failed to get users count: {response.status_code} - {response.text}')
                return None
            except httpx.RequestError as e:
                logger.error(f'Error getting users count: {e}')
                return None