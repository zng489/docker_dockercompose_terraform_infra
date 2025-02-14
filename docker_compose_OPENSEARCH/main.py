# Configuração simplificada do cliente OpenSearch
from opensearchpy import OpenSearch
host = 'localhost'
port = 9200
auth = ('admin', 'J!x2Vb9z*') # For testing only. Don't store credentials in code.
ca_certs_path = '/full/path/to/root-ca.pem' # Provide a CA bundle if you use intermediate CAs with your root CA.

# Create the client with SSL/TLS enabled, but hostname verification disabled.
client = OpenSearch(
    hosts = [{'host': host, 'port': port}],
    http_compress = True, # enables gzip compression for request bodies
    http_auth = auth,
    use_ssl = True,
    verify_certs = False,
    ssl_assert_hostname = False,
    ssl_show_warn = False,
    ca_certs = ca_certs_path
)

print(client.info()) # Get the cluster health


# Create an index with non-default settings.
index_name = 'python-test-index'
index_body = {
    'settings': {
        'index': {
            'number_of_shards': 2
        }
    }
}
 
response = client.indices.create(index_name, body=index_body)
print('\nCreating index:')
print(response)
 
document = {
    'title': 'Moneyball',
    'director': 'Bennett Miller',
    'year': '2011'
}
id = '1'
 
response = client.index(
    index=index_name,
    body=document,
    id=id,
    refresh=True
)
 
print('\nAdding document:')
print(response)
 
q = 'miller'
query = {
    'size': 5,
    'query': {
        'multi_match': {
            'query': q,
            'fields': ['title^2', 'director']
        }
    }
}
 
response = client.search(
    body=query,
    index=index_name
)
print('\nSearch results:')
print(response)


"""
response = client.delete(
    index=index_name,
    id=id
)
 
print('\nDeleting document:')
print(response)
 

response = client.indices.delete(index=index_name)
 
print('\nDeleting index:')
print(response)
"""