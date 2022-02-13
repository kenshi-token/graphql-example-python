import requests

# This is the Kenshi Deep Index endpoint for GraphQL
endpoint = "https://api.kenshi.io/index/graphql"

# Define your GraphQL query here
query = """{
    getEntries(blockchain: "binance-testnet") {
        event {
            name
        }
    }
}"""

# Post request sending the GraphQL query to the
# Kenshi Deep Index endpoint
response = requests.post(endpoint, json={"query": query})

# Receive the data and print it
data = response.json()["data"]
print(data)
