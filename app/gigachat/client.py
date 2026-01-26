import asyncio
import json
from logging import getLogger
import time
import httpx

from config import constants, settings
import uuid


class GigaChatClientExeption(Exception): ...


log = getLogger(__name__)


class GigaChatClient:
    def __init__(self):
        self.access_token: str | None = None
        self.is_active_schedual: bool = False
        self.schedual_task: asyncio.Task | None = None

    async def refresh_access_token_loop(self, expire_at: float):
        while self.is_active_schedual:
            try:
                await asyncio.sleep(expire_at - time.time() - 10)
                await self.refresh_access_token()

            except Exception as e:
                self.is_active_schedual = False
                raise e from None

    async def refresh_access_token(self) -> dict:
        data = await self._get_access_token()
        self.access_token = data["access_token"]
        log.info("Success refresh access token, new expire: %d", data["expires_at"])
        return data

    async def connect(self):
        data = await self.refresh_access_token()
        if not self.is_active_schedual and self.schedual_task is None:
            self.is_active_schedual = True
            self.schedual_task = asyncio.create_task(
                self.refresh_access_token_loop(data["expires_at"])
            )

    async def disconnect(self):
        if self.is_active_schedual:
            self.is_active_schedual = False

        if self.schedual_task:
            try:
                self.schedual_task.cancel()
                await self.schedual_task
            except asyncio.CancelledError:
                pass

    async def _get_access_token(self, *, scope: str = "GIGACHAT_API_PERS") -> dict:
        url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
        payload = {"scope": scope}
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
            "RqUID": str(uuid.uuid4()),
        }

        async with httpx.AsyncClient(verify=False) as client:
            response = await client.post(
                url,
                data=payload,
                headers=headers,
                auth=httpx.BasicAuth(
                    settings.llm_client_id, settings.llm_client_secret
                ),
            )
            data = response.json()

            return data

    def _get_system_promt(self) -> str:
        with open(constants.SYS_PROMT_PATH, encoding="utf-8") as f:
            sys_promt = f.read()
            return sys_promt

    async def send_roadmap_promt(self, prompt: str) -> dict[str, list[str | None]]:
        if self.access_token is None:
            raise GigaChatClientExeption("Missing access token")
        msg = {
            "model": "GigaChat",
            "messages": [
                {"content": self._get_system_promt(), "role": "system"},
                {
                    "content": prompt,
                    "role": "user",
                },
            ],
            "stream": False,
            "repetition_penalty": 1,
        }

        async def send_req() -> httpx.Response:
            async with httpx.AsyncClient(verify=False) as client:
                response = await client.post(
                    "https://gigachat.devices.sberbank.ru/api/v1/chat/completions",
                    json=msg,
                    headers={
                        "Content-Type": "application/json",
                        "Authorization": f"Bearer {self.access_token}",
                    },
                )

            print(f"Результат: {response.json()}")
            return response

        fail_counter = 0
        while fail_counter < 2:
            response = await send_req()
            if response.status_code == 200:
                break
            if response.status_code == 401:
                await self.refresh_access_token()
                fail_counter += 1
                asyncio.sleep(1)
            else:
                break

        raw_json = response.json()["choices"][0]["message"]["content"]
        return json.loads(raw_json)


gigachat_client = GigaChatClient()
