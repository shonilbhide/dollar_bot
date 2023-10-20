# About DollarSplitBot's /delete_expense Feature
This feature is a part of a program, and its purpose is to manage a list of registered users and allow the deletion of a user from this list via a chatbot

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/shonilbhide/dollar_bot/blob/main/code/delete_user.py)

# Code Description
## Functions

1: `delete_user(message, bot, user_list)`
This function is responsible for deleting a registered user from the list. Here's what it does:

- It takes three arguments: `message` (a message object received from the user), `bot` (the Telegram bot object), and `user_list` (a dictionary containing information about registered users).
- It first checks if there are any users to delete. If there are no users, it informs the user that no users are registered for deletion.
- If there are registered users, it creates a custom keyboard with a list of user names and sends a message to the user to select which user they want to delete.
- It registers a "next step handler" to capture the user's choice and proceeds to the `confirm_delete` function for further processing.

2. 2: `confirm_delete(message, bot, user_list)`
This function is called after the user selects a user to delete. Here's what it does:

- It takes three arguments: `message` (the user's message with the selected user name), `bot` (the Telegram bot object), and `user_list` (the dictionary with user information).
- It checks if the selected user exists in the list of registered users. If the user is found, it removes the user's information from the `user_list` dictionary.
- It also updates the user list by removing the user's name.
- It saves the updated `user_list` to a file (possibly for future reference).
- It informs the user that the user has been deleted successfully.
- If there are no users left in the list after deletion, it notifies the user. Otherwise, it shows the updated list of registered users.
- Finally, it removes the custom keyboard to allow the user to use other commands.

# How to run this feature?

Rutuja Rashinkar, [19-10-2023 10:48 PM]
/delete_user

My_MyDollarBot_bot, [19-10-2023 10:49 PM]
Select the user you want to delete:

Rutuja Rashinkar, [19-10-2023 10:49 PM]
A

My_MyDollarBot_bot, [19-10-2023 10:49 PM]
A has been deleted successfully.

My_MyDollarBot_bot, [19-10-2023 10:49 PM]
Updated list of registered users:
Rutuja Rashinkar
 B
 C
 Proff
 Sorr