tries = 1
print("try to connecting to server......... ")

while tries <= 3:
    print(f"try {tries}")
    if tries == 3:
        print("connected...!")
        break
    tries += 1

files = ["app.log", "error.txt", "system.log", "data.csv"]

for f in files:
    if f.endswith(".log"):
        print(f"Log Files: {f}")

instances = ["i-123", "i-555", "db-22", "i-999"]

for i in instances:
    if i.startswith("i"):
        print(f"instances with i: {i}")
    