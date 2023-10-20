# About MyDollarBot's budget_view module
The budget_view module contains all the functions required to implement the display add and update features. In essence, all operations involved in addition to a new budget and updating an existing budget are taken care of in this module and are implemented here. 

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/shonilbhide/dollar_bot/blob/Issue_92_Documentation/code/budget_update.py)

# Code Description
## Functions
run(message, bot):

This function is the entry point for the "UPDATE BUDGET" feature. It presents the user with a menu to select a budget type (either overall or by category).
It checks if the user's chat ID is in the user list and initializes the user's data if not already present.
It uses the Telegram Bot API to create a menu with available budget types and then waits for the user to make a selection.
After the user makes a selection, it registers a handler for the next step, which is either setting the overall budget or selecting a category for the budget.
set_budget_type(message, bot, user_list):

This function is called when the user selects a budget type (overall or category).
It checks if the selected budget type is valid and proceeds accordingly.
If the user selects "overall," it calls the set_overall_budget function.
If the user selects "category," it calls the set_category_budget function.
set_overall_budget(message, bot, user_list):

This function is responsible for setting the overall budget.
It prompts the user to enter the overall budget and registers a handler to save the entered budget.
save_overall_budget(message, bot, user_list):

This function handles the user input for the overall budget.
It validates the input and stores the overall budget in the user's data.
The budget is saved in a dictionary structure, and the user's data is written back to a JSON file.
set_category_budget(message, bot, user_list):

This function is responsible for setting the budget for a specific spending category.
It presents the user with a menu to select a category for budgeting.
set_category_budget_amount(message, bot, user_list):

This function is called after the user selects a spending category for budgeting.
It prompts the user to enter the budget amount for the selected category and registers a handler to save the entered amount.
save_category_budget(message, bot, user_list, category):


# How to run this feature?
Once the project is running(please follow the instructions given in the main README.md for this), please type /budget into the telegram bot. Please follow the prompts on the screen to create a new budget.
