Bot = type(
    'Bot',
    (),
    {
        'name': '',
        'say_name': lambda self: print(self.name),
        'send_message': lambda self, message: print(message),
        '__init__': lambda self, name: setattr(self, 'name', name),
    }
)

TelegramBot = type(
    'TelegramBot',
    (Bot,),
    {
        'url': '',
        'chat_id': None,
        'set_url': lambda self, url: setattr(self, 'url', url),
        'set_chat_id': lambda self, chat_id: setattr(self, 'chat_id', chat_id),
        'send_message': lambda self, message: print(f"{self.name} bot says {message} to chat {self.chat_id} using {self.url}")
    }
)


# checking the correctness of the work program
some_bot = Bot("Marvin")
some_bot.say_name()
some_bot.send_message("Hello")

telegram_bot = TelegramBot("TG")
telegram_bot.say_name()
telegram_bot.set_url(2)
telegram_bot.set_chat_id(2)
telegram_bot.send_message("Hello")
