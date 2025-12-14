
tools = ["AWS", "Docker", "Jenkins", "Terraform", "Git", "Python"]

for t in tools:
    if t.startswith("D") or t.startswith("T"):
        print(t)


numbers = [12, 5, 23, 7, 18, 2]

for n in numbers:
    if n > 10:
        print(n)

text = "Welcome to DevOps automation"

for t in text:
    if t in "aeiosAEIOU":
        print(t)