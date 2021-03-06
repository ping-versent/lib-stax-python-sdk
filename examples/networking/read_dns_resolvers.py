import os

from staxapp.config import Config
from staxapp.openapi import StaxClient

Config.access_key = os.getenv("STAX_ACCESS_KEY")
Config.secret_key = os.getenv("STAX_SECRET_KEY")

networks = StaxClient("networking")

# query all resolvers within your organisation, or provide a resolver id
response = networks.ReadDnsResolvers(dns_resolver_id="<resolver_uuid>")

print(response.json())