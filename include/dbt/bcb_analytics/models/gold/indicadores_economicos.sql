select
    s.data,
    s.codigo_serie,
    n.nome_indicador,
    s.valor
from {{ ref('sgs_series') }} as s
left join {{ ref('nome_series_sgs') }} as n
    on s.codigo_serie = n.codigo_serie
