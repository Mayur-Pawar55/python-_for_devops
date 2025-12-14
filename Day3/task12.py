

def validate_tools(tools):
    if tools == "Docker" or tools == "Kubernetes":
        print("Containerization tools")
    else:
        print("Unknown Tools")


tools = ["Docker", "Terraform", "Kubernetes", "Git"]
for t in tools:
    validate_tools(t)