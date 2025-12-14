def server_check(server):
    if server.startswith("db"):
        print(f"DB Server")
    else:
        print("Normal server")
    
servers = ["web1", "db1", "app", "db2"]

for s in servers:
    server_check(s)