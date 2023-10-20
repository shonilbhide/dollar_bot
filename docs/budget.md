# About MyDollarBot's /budget Feature
This feature enables the user to add, remove, edit, or display a budget in their expense tracker. The user can choose between an overall expense tracker, which counts every expense made to the budget, or a category-wise expense tracker, which only counts expenses in a particular category towards the budget for that category.

The user can choose a category and add the amount for the budget to be stored in the expense tracker.

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/shonilbhide/dollar_bot/blob/Issue_92_Documentation/code/budget.py)

# Code Description
## Functions

- run(message, bot):
This function is the entry point for the BUDGET feature.
It displays a menu in the Telegram bot where the user can select an operation, such as adding an expense, updating an expense, viewing their budget, or deleting an expense.
It takes two arguments: message (the user's message) and bot (the Telegram bot object).

- post_operation_selection(message, bot):
After the user selects an operation in the menu, control is passed to this function.
It processes the user's choice and performs the selected operation, such as adding, updating, viewing, or deleting expenses.
It also handles cases where the user's input is invalid.
This function takes two arguments: message (the user's message) and bot (the Telegram bot object).
Various operation-specific functions (budget_update.run, budget_view.run, budget_delete.run):
These functions are called when the user selects a specific operation (e.g., add, update, view, delete) in the menu.
They handle the specific operation's logic, such as adding an expense, updating a budget, viewing expenses, or deleting expenses.

- helper.write_json(user_list):
This function is used to save the user's budget and expense data to a JSON file, so it can be retrieved later.
In summary, the BUDGET feature in this code allows users to interact with a Telegram bot to manage their budget and expenses. Users can perform various operations related to their budget, and the code handles each operation accordingly. The user's data is stored in a JSON file for future reference.


# How to run this feature?
Once the project is running(please follow the instructions given in the main README.md for this), please type /budget into the telegram bot.
