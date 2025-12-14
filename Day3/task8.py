def server_check(server):
    if server.startswith("db"):
        print(f"Checking {server} is databse server")
    else:
        print(f"Checking {server} is Application server")
servers = ["web1", "db1", "app1", "db2", "cache"]

for s in servers:
    server_check(s)
    