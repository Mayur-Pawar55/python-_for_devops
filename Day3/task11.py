def is_database_server(server):
    return server.startswith("db")

servers = ["web", "db1", "app", "db2", "db3"]

count = 0

for s in servers:
    if is_database_server(s):
        count += 1

print("Total Database servers:", count)
