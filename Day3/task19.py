#Count how many database servers are in a server list.

servers = ["db1", "db2", "apache", "cache", "db3"]
count = 0
for s in servers:
    if s.startswith("db"):
        count += 1

print(f"Total no of database server is:{count}")