
#Scan multiple log lines and print only error lines.

def error_check(line):
    if "error" in line:
        print("error found!")
    else:
        print("OK")

logs = [
    "ec sdcs error",
    "error is not available",
    "forbidden",
    "error 403"
]

for l in logs:
    error_check(l)