import httpx
import asyncio
from typing import Any, Dict

from src.config import URL_BASE_API


async def get_deputados_by_name(name: str) -> Dict[str, Any] | None:
    """Busca deputados pelo nome na API da Câmara dos Deputados"""
    async with httpx.AsyncClient() as client:
        try:
            params = {
                "nome": name,
                "ordem": "ASC",
                "ordenarPor": "nome"
            }
            response = await client.get(
                f"{URL_BASE_API}/deputados",
                params=params,
                timeout=30.0)

            response.raise_for_status()
            data = response.json()

            deputies_list = data.get('dados', [])
            if not deputies_list:
                return None  # Return empty result if no deputies found
            
            # Get details for limited deputies found
            deputies_details = []
            for deputy in deputies_list:
                deputy_id = deputy.get('id')
                if deputy_id:
                    try:
                        deputy_details = await get_deputy_details(deputy_id)
                        if deputy_details and 'dados' in deputy_details:
                            deputies_details.append(deputy_details['dados'])
                        else:
                            # If details not found, use basic info from search
                            deputies_details.append(deputy)
                    except Exception as e:
                        # If error getting details, use basic info
                        print(f"Warning: Could not get details for deputy {deputy_id}: {e}")
                        deputies_details.append(deputy)
            
            # Return in the same format as the original API
            return {
                'dados': deputies_details,
                'links': data.get('links', []),
                'metadados': data.get('metadados', {})
            }
        except httpx.RequestError:
            return None


async def get_deputy_details(deputy_id: int) -> Dict[str, Any] | None:
    """Busca detalhes de um deputado específico pelo ID"""
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{URL_BASE_API}/deputados/{deputy_id}", timeout=30.0)
            response.raise_for_status()
            return response.json()
        except httpx.RequestError:
            return None


# Move the runnable debug entrypoint here so functions are defined before use
# if __name__ == "__main__":
#     async def _debug_run():
#         result = await get_deputados_by_name("Eduardo")
#         print(result)
#
#     # Run the async entrypoint so the module can be executed directly for debugging
#     asyncio.run(_debug_run())
