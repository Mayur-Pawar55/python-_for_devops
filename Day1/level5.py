"""
server = ["web1", "web2", "db1", "cache1", "db2"]

for s in server:
    print(f"Cheching Server: {s}")
    if s.startswith("db"):
        print("Database server detected!")


servers = ["web1", "db1", "app", "db2", "cache", "db3", "db5"]
count = 0
for s in servers:
    if s.startswith("db"):
        count += 1
print("Total DB servers:", len(s))
        """

servers = ["web1", "db1", "app", "db2q", "cache", "db3", "db5"]
count = 0
for s in servers:
    if s.startswith("db"):
        count += 1
print("Total DB servers:", count)
        