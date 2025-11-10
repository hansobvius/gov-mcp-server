import httpx
import asyncio
from typing import Any, Dict

from src.config import URL_BASE_API

# Check for deputy front lines inside the API of Câmara dos Deputados
async def get_front_line_by_deputy(id: str) -> Dict[str, Any] | None:
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{URL_BASE_API}/deputados/{id}/frentes", timeout=30.0)
            response.raise_for_status()
            return response.json()
        except httpx.RequestError:
            return None