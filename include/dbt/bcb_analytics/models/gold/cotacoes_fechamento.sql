select
    p.moeda,
    m.nomeformatado as nome_moeda,
    p.datahoracotacao::date as data_cotacao,
    p.cotacaocompra,
    p.cotacaovenda
from {{ ref('ptax_cotacoes') }} as p
left join {{ ref('moedas') }} as m
    on p.moeda = m.simbolo
where p.tipoboletim = 'Fechamento'
