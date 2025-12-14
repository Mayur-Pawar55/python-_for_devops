

def retry_connection(num):
    while num <= 3:
        print(f"connecting....{num}")
        if num == 3:
            break
        num += 1
    print("Connected!")
    
retry_connection(1)

