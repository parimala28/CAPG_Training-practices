class Payment:
    def process_payment(self,amount):
          print(f"The payment {amount:.2f}")

class CreditCardPayment(Payment):
    def process_payment(self,amount):
        print(f"The processing is done by credi card {amount:.2f}.")
class PayPalPayment(Payment) :
    def process_payment(self,amount):
        print(f"The processing is done by pay pal {amount:.2f}.")

class BitcoinPayment(Payment):
    def process_payment(self,amount):
        print(f"The processing is done by bitcoin {amount:.2f}.")  

p=Payment()
p.process_payment(30)
p=PayPalPayment()
p.process_payment(40)
p=BitcoinPayment()
p.process_payment(70)

