import time
from plyer import notification
if __name__=='__main__':
    while True:
        notification.notify(
            title='ALER!!!',
            message="Take a break",timeout=10
            )
        time.sleep(3600)

        
        