class Message:

    def get_content():
        pass

class TextMessage(Message):
    def __init__(self, content):
        self.content = content

    def get_content(self):
        return f"SMS {self.content}"
        

class EmailMessage(Message):
    def __init__(self, content):
        self.content = content

    def get_content(self):
        return f"Email {self.content}"

class PushNotification(Message):
    def __init__(self, content):
        self.content = content

    def get_content(self):
        return f"Notification {self.content}"
    

sms = TextMessage(content="Zpráva: Dobrý den, Vaše objednávka byla právě odeslána. Děkujeme za nákup!  ")

email = EmailMessage(content="From: odesilatel@example.com\nTo: prijemce@example.com\nSubject: Předmět zprávy  Dobrý den,  toto je ukázkový text e-mailové zprávy.")

push = PushNotification(content="Zpráva: Máš novou notifikaci! Klikni pro více informací.")

class MessageFactory:

    possible = ["sms", "email", "push"]

    def createMessage(self, message_type):
        if message_type == "sms":
            return TextMessage(self)
        elif message_type == "email":
            return EmailMessage(self)
        elif message_type == "push":
            return PushNotification(self)
        else:
            print("Neznámý typ zprávy")

        if message_type in MessageFactory.possible:
            return globals()[message_type]()
        else:
            pass

factory = MessageFactory()
message1 = factory.createMessage("sms")
message2 = factory.createMessage("email")
message3 = factory.createMessage("push")
print(message1.get_content())
print(message2.get_content())
print(message3.get_content())
