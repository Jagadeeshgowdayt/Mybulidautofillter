import telegram
import re

def filter_files(bot, update, keyword):
    # Get the chat id
    chat_id = update.effective_chat.id

    # Get the list of files in the chat
    files = bot.get_file_list(chat_id)

    # Filter the files by keyword
    filtered_files = []
    for file in files:
        if re.search(keyword, file.file_name):
            filtered_files.append(file)

    # Send a message to the chat with the filtered files
    bot.send_message(chat_id, "Here are the files that contain the keyword `{}`: ".format(keyword))
    for file in filtered_files:
        bot.send_message(chat_id, file.file_name)

if __name__ == "__main__":
    # Create a Telegram bot
    bot = telegram.Bot(token="YOUR_BOT_TOKEN")

    # Set the keyword to filter by
    keyword = "keyword"

    # Start filtering files
    while True:
        update = bot.get_updates()[-1]
        filter_files(bot, update, keyword)
￼Enter
