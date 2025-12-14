#Check if a given server is a database server.

def server_check(server):
    if server.startswith("db"):
        print(f"{server} is database server")
    else:
        print("unknown server")


servers = ["db1", "apache", "cache", "db2"]
for s in servers:
    server_check(s)