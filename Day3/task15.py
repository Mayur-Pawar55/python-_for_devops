#Keep checking server health until it becomes healthy.
import time
def server_health(health):
    print("checking server health")

    while health != "healthy":
        time.sleep(3)
        print("server is not in healthy condition, cheching again....")


server_health("unhealthy")