select
    simbolo,
    nomeformatado,
    tipomoeda
from {{ source('bronze', 'moedas') }}
