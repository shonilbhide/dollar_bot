import helper

# === Documentation of delete.py ===


def run(message, bot):
    """
    run(message, bot): This is the main function used to implement the delete feature.
    It takes 2 arguments for processing - message which is the message from the user, and bot
    which is the telegram bot object from the main code.py function. It calls helper to get the user
    history i.e chat ids of all user in the application, and if the user requesting a delete has their
    data saved in myDollarBot i.e their chat ID has been logged before, run calls the deleteHistory(chat_id):
    to remove it. Then it ensures this removal is saved in the datastore.
    """
    global user_list
    chat_id = message.chat.id
    delete_history_text = ""
    user_list = helper.read_json()

    msg = bot.send_message(chat_id, "Do you want to delete complete history? Y/N")
    bot.register_next_step_handler(msg, delete_history, bot)


def delete_history(message, bot):
    chat_id = message.chat.id
    if str(message.text) == "Y" or str(message.text) == "y":
        if str(chat_id) in user_list:
            helper.write_json(deleteHistory(chat_id))
            delete_history_text = "History has been deleted!"
        else:
            delete_history_text = "No records there to be deleted. Start adding your expenses to keep track of your spendings!"
        bot.send_message(chat_id, delete_history_text)
    elif str(message.text) == "N" or str(message.text) == "n":
            delete_history_text = "History not deleted."
            bot.send_message(chat_id, delete_history_text)
    else:
            msg = bot.send_message(chat_id, "Cannot recognize the character. Enter Y/N.")
            bot.register_next_step_handler(msg, delete_history, bot)       
    

# function to delete a record
def deleteHistory(chat_id):
    """
    deleteHistory(chat_id): It takes 1 argument for processing - chat_id which is the
    chat_id of the user whose data is to deleted from the user list. It removes this entry from the user list.
    """
    global user_list
    if str(chat_id) in user_list:
        del user_list[str(chat_id)]
    return user_list
