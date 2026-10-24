-- Executado automaticamente na PRIMEIRA criação do container (volume vazio).
create schema if not exists bronze;
create schema if not exists silver;
create schema if not exists gold;

comment on schema bronze is 'Dados brutos das APIs do BCB, gravados pelo Airbyte';
comment on schema silver is 'Dados tipados, limpos e deduplicados (dbt)';
comment on schema gold   is 'Modelos prontos para consumo (dbt)';
