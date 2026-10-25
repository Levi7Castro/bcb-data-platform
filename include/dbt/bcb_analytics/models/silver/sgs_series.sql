select
    to_date(data, 'DD/MM/YYYY') as data,
    valor::numeric as valor,
    codigo_serie::integer as codigo_serie
from {{ source('bronze', 'sgs_series') }}
