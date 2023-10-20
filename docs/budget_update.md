# About MyDollarBot's budget_view module
The budget_view module contains all the functions required to implement the display add and update features. In essence, all operations involved in addition to a new budget and updating an existing budget are taken care of in this module and are implemented here. 

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/shonilbhide/dollar_bot/blob/Issue_92_Documentation/code/budget_view.py)

# Code Description
## Functions

- run(message, bot)
This is the main function responsible for implementing the "VIEW BUDGET" feature. When a user interacts with the application, it first checks if an overall budget or category-wise budget is available for that user. Depending on the available budget, it either displays the overall budget or the category-wise budget. If no budget is available, it raises an exception with a message suggesting that the user should add or update their budget.
It takes two arguments: message, which is the user's message or interaction, and bot, which is the bot used to send responses.

- display_overall_budget(message, bot)
This function is called when there is an overall budget available for the user. It retrieves the overall budget, converts it to a string, and then sends a message to the user with the overall budget information.
It takes two arguments: message, which is the user's message, and bot, which is used to send responses.

- display_category_budget(message, bot)
This function is called when there is a category-wise budget available for the user. It retrieves the category-wise budget data, formats it into a string, and sends a message to the user with the category-wise budget information.
It takes two arguments: message, which is the user's message, and bot, which is used to send responses.
The purpose of this code is to provide the user with a way to view their budget information. It checks whether an overall budget or category-wise budget is available and then displays the relevant budget details to the user. If no budget information is available, it informs the user that they should first add or update their budget.


# How to run this feature?
Once the project is running(please follow the instructions given in the main README.md for this), please type /budget into the telegram bot. Please follow the prompts on the screen to create a new budget.
