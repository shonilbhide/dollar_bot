# About MyDollarBot's budget_delete module
The DELETE BUDGET feature is part of a program or bot that helps users manage their budgets and expenses. This specific feature allows users to delete their budget data if they no longer wish to track their financial information. 

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/shonilbhide/dollar_bot/blob/Issue_92_Documentation/code/budget_delete.py)

# Code Description
## Functions


About the DELETE BUDGET Feature
The DELETE BUDGET feature is part of a program or bot that helps users manage their budgets and expenses. This specific feature allows users to delete their budget data if they no longer wish to track their financial information.

Location of Code for this Feature
The code that implements this feature can be found in the main file of the project, likely in the same repository where the bot is hosted.

Code Description
Functions
run(message, bot):
This is the main function responsible for implementing the DELETE BUDGET feature. It performs the following steps:

It receives a message and a bot object as arguments. The message typically comes from a user interacting with the bot.
It checks if the chat (user) has budget data. If the user doesn't have any budget data, it sends a message to inform the user.
If the user does have budget data, it proceeds to delete the budget data. This involves setting the budget data to empty values, effectively erasing it.
After deleting the budget data, it saves the updated user information.
Finally, it sends a message to the user to confirm that the budget data has been successfully deleted.
helper.read_json():
This function is not shown in the provided code, but it is assumed to be used to read user data from a JSON file or storage.

helper.write_json(user_list):
This function is not shown in the provided code, but it is assumed to be used to write the updated user data back to a JSON file or storage.


# How to run this feature?
Once the project is running(please follow the instructions given in the main README.md for this), please type /budget into the telegram bot. Add a budget and then type /budget again. Please choose the option for deleting a budget.
