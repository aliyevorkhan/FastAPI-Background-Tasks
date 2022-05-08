from fastapi import BackgroundTasks, FastAPI
from time import sleep

app = FastAPI()

count=0

def write_notification(count, email: str, message=""):
    with open("log.txt", mode="a+") as email_file:
        content = f"notification for {email}: {message} {str(count)}\n"
        email_file.write(content)
        sleep(3)


@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    global count
    count+=1
    background_tasks.add_task(write_notification, count, email, message="some notification")
    return {"message": "Notification sent in the background"}