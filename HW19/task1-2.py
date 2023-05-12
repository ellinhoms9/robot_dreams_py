class Bot:
    def __init__(self, name):
        self.name = name


    def say_name(self):
        print(self.name)


    def send_massage(self, message):
        print(message)


class TelegramBot(Bot):
    def __init__(self, name, url=None, chat_id=None):
        super().__init__(name)
        self.url = url
        self.chat_id = chat_id


    def send_message(self, message):
        print(f"{self.name} bot says {message} to chat {self.url} using {self.chat_id}.")


    def set_url(self, url):
        self.url = url


    def set_chat_id(self, chat_id):
        self.chat_id = chat_id


# checking the correctness of the work program
some_bot = Bot("Marvin")
some_bot.say_name()
some_bot.send_massage("Hello")

telegram_bot = TelegramBot("TG")
telegram_bot.say_name()
telegram_bot.set_url(2)
telegram_bot.set_chat_id(2)
telegram_bot.send_message("Hello")
