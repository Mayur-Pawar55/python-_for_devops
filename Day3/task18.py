#Retry API call maximum 3 times.
import time


def api_call(attempt):
    while attempt <= 3:
        print(f"API Call Attempt {attempt}")
        api_status = "failed"
        if api_status == "success":
            print("API Call Successfull")
            break
        else:
            print("API call get failed, retry")
            time.sleep(3)
            attempt += 1

api_call(1)