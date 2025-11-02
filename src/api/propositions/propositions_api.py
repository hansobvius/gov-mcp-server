import httpx
import asyncio
from typing import Any, Dict

from src.api.deputies.deputies_api import get_deputados_by_name
from src.config import URL_BASE_API

async def get_propositions_by_id(proposition_id: str) -> Dict[str, Any] | None:
    """Busca proposições pelo ID na API da Câmara dos Deputados"""
    async with httpx.AsyncClient() as client:
        try:
            params = {
                "idDeputadoAutor": proposition_id,
                "ordem": "ASC",
                "ordenarPor": "id"
            }
            response = await client.get(
                f"{URL_BASE_API}/proposicoes",
                params=params,
                timeout=30.0)

            response.raise_for_status()
            data = response.json()

            proposition_list = []
            propositions_list = data.get('dados', [])
            if propositions_list:
                for proposition in propositions_list:
                    proposition_id = proposition["id"]
                    if proposition_id:
                        try:
                            proposition_detail = await get_proposition_details(proposition_id)
                            if proposition_detail and 'dados' in proposition_detail:
                                proposition_list.append(proposition_detail["dados"])
                        except Exception as e:
                            print(print(f"Warning: Could not get details for deputy {proposition_id}: {e}"))
            return {
                'dados': proposition_list,
                'links': data.get('links', []),
            }
        except httpx.RequestError:
            return None


async def get_proposition_details(proposition_id: str) -> Dict[str, Any] | None:
    """Busca detalhes de uma proposição específica pelo ID"""
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{URL_BASE_API}/proposicoes/{proposition_id}", timeout=30.0)
            response.raise_for_status()
            data = response.json()
            return data
        except httpx.RequestError:
            return None

# Move the runnable debug entrypoint here so functions are defined before use
# if __name__ == "__main__":
#     async def _debug_run():
#         result = await get_deputados_by_name("Eduardo")
#         propositions = await get_propositions_by_id(result['dados'][0]['id'])
#         print(propositions)
#
#     # Run the async entrypoint so the module can be executed directly for debugging
#     asyncio.run(_debug_run())