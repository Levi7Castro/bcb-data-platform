import os
import yaml
import airbyte as ab
from airbyte.caches import PostgresCache

with open("source_bcb.yaml") as f:
    manifest = yaml.safe_load(f)

cache = PostgresCache(
    host=os.environ.get("DW_HOST", "localhost"),
    port=int(os.environ["DW_PORT"]),
    username=os.environ["DW_USER"],
    password=os.environ["DW_PASSWORD"],
    database=os.environ["DW_DATABASE"],
    schema_name="bronze",
)

source = ab.get_source(
    "source-declarative-manifest",
    config={},
    streams=["moedas", "sgs_series", "ptax_cotacoes"],
    source_manifest=manifest,
)

source.check()

result = source.read(cache=cache, write_strategy="merge")
print(result.processed_records)
