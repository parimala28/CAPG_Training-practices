class Notification:
    def send(self,msg):
        print(f"The notification is came {msg}")
class EmailNotification(Notification):
    def send(self,msg):
        print(f"The notification {msg}")

class SMSNotification(Notification): 
    def send(self,msg):
        print(f"The notification {msg}") 

email=EmailNotification()
email.send("message by email")
sms=SMSNotification()
sms.send("message by sms")             