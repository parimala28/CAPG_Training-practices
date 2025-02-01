class Logger:
    def log(self,message,msg='Error'):
        if msg == 'Error':
            print(f"error: {message}.")
        elif msg == 'warning':
            print(f" warning: {message}")
        elif msg == 'Info':
            print(f"Info: {message}")
        else:
            return "Unknow"

log=Logger()
log.log("This is ERROR message", "Error")
log.log("This is WARNING message", "warning")
log.log("This is INFO message","Info")

                   