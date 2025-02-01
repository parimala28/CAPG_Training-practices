from abc import ABC ,abstractmethod
class Mail(ABC):
    @abstractmethod
    def send(self):
        pass

class Email(Mail):
    def send(self):
        print("email has send")

class SMS(Mail):
    def send(self):
        print("sms has send")     

class WhatsApp(Mail):
    def send(self):
        print("WhatsApp message has send")
            

e=Email()
s=SMS()
w=WhatsApp()

e.send()
s.send()
w.send()

    

    
