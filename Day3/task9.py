

def scan_log(line):
    if "ERROR" in line:
        print("Error found!")
    else:
        print("OK")
    
logs = [
    "INFO Server started",
    "ERROR Disk full",
    "INFO User login",
    "ERROR Memory leak"
]

for l in logs:
    scan_log(l)