Hey _Geek!_ <br>
Here is a small guide to get you started with `“Telegram Bots using Python”`.

### Prerequisites:
- [x] Python 3.6 or higher
- [x]	Telegram Account and App
- [x]	python-telegram-bot library
- [x]	Any IDE of your choice

> Install Library: pip install python-telegram-bot

### About the library:
In this library,  `telegram.ext`  submodule is a built in and top of the pure API implementation.
It contains several classes, but two of them are most important.
1. telegram.ext.Updater
1. telegram.ext.Dispatcher

The `Updater` class continuously fetches new updates from the telegram and passes them on to the `Dispatcher` class. Creating an `Updater object` automatically creates a `Dispatcher` for us and link them together with a `Queue`. Then we can register `Handlers` of different types to the `Dispatcher`, which will sort the updates fetched by the `Updater` according to the handlers we registered and deliver them to a `callback function` that we will define.

Every Handler is an instance of any subclass of the `telegram.ext.Handler` subclass. We can also create our own handler.

### Getting Access Token:
Now we need to chat with [@BotFather](https://telegram.me/BotFather) in order to get Access Token of our bot.<br>
Open a chat with [@BotFather](https://telegram.me/BotFather) in your Telegram App.<br>
Use the following commands:
- /newbot --> creates new bot.
- /mybots --> see all your bots
- /token  --> to get token of your bot (**Don’t Share this Token with anyone**)

### Once you get the Token, fire up your IDE and let get started 🚀
First we need to create an updater Object.
```py
from telegram.ext import Updater
updater = Updater("Your ACCESS TOKEN here")
```
As mentioned above, Updater Object has created dispatcher for us, we can save it in a variable for quicker access.
```py
dispatcher = updater.dispatcher
```
Setting up Logging
```py
import logging
logging.basicConfig( format = "%(asctime)s - %(name)s - %(levelname)s -%(message)s",
			        level=logging.INFO)
logger = logging.getLogger(__name__)
```

Now we will define a function that should process  a specific type of update:
```py
def start(update, context):
context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, this is Rajasthani Geek’s Bot")
```

Now, our goal is to call this function every time Bot receives a telegram Message/Command `/start` ,To do this we need to use a CommandHandler and register it to our dispatcher.
```py
from telegram.ext import CommandHandler
start_handler = CommandHandler(‘start’, start)
dispatcher.add_handler(start_handler)
```
In the CommandHandler , `'start'` indicates Command and second `start` is the callback function that get called every time Bot receives `'start'` command i.e. `/start` message.

Now we are good to go and run our first Telegram Bot.
```py
updater.start_polling()
```

Now when you'll go to your bot @username_of_bot and type `'/start'` command, it will respond to you with our declared message: `"Hello, this is Rajasthani Geek’s Bot"`


**Now we are familiar to create a bot that responds to a command, we just have to create a callback function, a handler of that function and add that handler to the dispatcher.**

## Echo Bot
Next, we will create a bot that will respond to every message. This bot will reply back your message, that’s why it called “Echo Bot”.

Callback function:
```py
def echo(update, context):
	user_message = update.message.text
	context.bot.send_message(chat_id=update.effective_chat.id, text=user_message)
```
We will use MessageHandler for this task, MessageHandler listens regular messages.
```py
from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)
```

Let's add some actual functionality to our bot. We want to implement a `/caps` command that will take some text as an argument and reply to it in CAPS. To make things easy, we can receive the arguments (as a `list`, split on spaces) that were passed to a command in the callback function:

```py
def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)
```

Another cool feature of the Telegram Bot API is the [inline mode](https://core.telegram.org/bots/inline). If we want to implement inline functionality for our bot, first we have to talk to [@BotFather](https://telegram.me/BotFather) and enable inline mode using `/setinline`.


```py
from telegram import InlineQueryResultArticle, InputTextMessageContent
def inline_caps(update, context):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, results)

from telegram.ext import InlineQueryHandler
inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)
```

What if a user send commands that are not included in our bot, we can use `MessageHandler` with a `Command` filter to reply to all unknown commands 😃
```
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)
```
**Note that, `unknown_handler` should be added to the dispatcher at last, otherwise it would get triggered before our other existing commands.**

That's all from our side, go ahed and experiment with your bot, Happy Learning 👍😄

## Join our Community!
- [Discord Server](https://discord.gg/bM9Wy6Yzn2)
- [Codecademy Chapter](https://community.codecademy.com/rajasthani-geeks/)
- [Instagram](https://www.instagram.com/pragmaticprogrammer/)
