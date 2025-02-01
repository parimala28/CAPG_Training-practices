from abc import ABC,abstractmethod
class UserAuthentication(ABC):
    @abstractmethod
    def login(self):
        pass
    @abstractmethod
    def logout(self):
        pass
class GoogleAuth(UserAuthentication):
    def login(self):
        print("user logged in using google authenticator.")
    def logout(self):
        print("user logged out from the Acc.")

class  FaceBookAuth(UserAuthentication):
    def login(self):
        print("user logged in using Facebook Authenticator.")
    def logout(self):
        print("user logged out from Acc.")

ga=GoogleAuth()
ga.login()
ga.logout()
fa=FaceBookAuth()
fa.login()
fa.logout()                         