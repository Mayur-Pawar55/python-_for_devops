def check_servers(server):
    if server.startswith("db"):
        print(f"{server} is databse server")
    else:
        print(f"{server} is normal server")

servers = ["web1", "db1", "cache1"]

for s in servers:
    check_servers(s)