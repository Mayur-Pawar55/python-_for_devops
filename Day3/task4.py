def retry_connection():
    tries = 1  
    while tries <= 3:
        print(f"trying...{tries}")
        if tries == 3:
            print("Connected")
            break
        tries += 1



retry_connection()