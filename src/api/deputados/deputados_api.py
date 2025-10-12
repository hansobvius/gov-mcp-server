import httpx

from typing import Any, Dict
from src.config import URL_BASE_API


async def get_deputados(name: str) -> Dict[str, Any]:
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(URL_BASE_API, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None