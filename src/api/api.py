from .deputies.deputies_api import get_deputados_by_name, get_deputy_details
from .propositions.propositions_api import get_propositions_by_id, get_proposition_details

# Exportar as funções para uso em outros módulos
__all__ = [
    'get_deputados_by_name',
    'get_deputy_details',
    'get_propositions_by_id',
    'get_proposition_details'
]