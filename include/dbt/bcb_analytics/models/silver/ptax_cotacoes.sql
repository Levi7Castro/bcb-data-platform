select
    datahoracotacao::timestamp as datahoracotacao,
    tipoboletim,
    moeda,
    paridadecompra,
    paridadevenda,
    cotacaocompra,
    cotacaovenda
from {{ source('bronze', 'ptax_cotacoes') }}
