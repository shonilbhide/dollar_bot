# About DollarSplitBot's /delete_expense Feature
This feature is part of a program that appears to be related to an expense tracking bot for a messaging platform like Telegram. The primary purpose is to implement a feature for deleting expense records.

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/shonilbhide/dollar_bot/blob/main/code/delete_expense.py)

# Code Description
## Functions

1. `run(m, bot)`: 
This function is the main entry point for the delete feature. It takes two arguments, `m` (a message from the user) and `bot` (a Telegram bot object). It displays a list of the user's expense records and asks the user to select an expense to delete. The user's selection is then passed to the `select_category_to_be_deleted` function for further processing.

2. `select_category_to_be_deleted(m, bot)`: 
This function handles the user's selection of an expense to delete. It takes the selected data as input and asks the user to confirm the deletion by typing "Y" or "N." The user's choice is then passed to the `delete_selected_data` function.

3. `delete_selected_data(message, bot, selected_data)`: 
This function handles the actual deletion of the selected expense data. It checks if the user has selected any data and then, if confirmed (by typing "Y" or "y"), deletes the selected record from the user's expense history. The updated expense history is saved, and the user is provided with feedback about the deleted record. Optionally, the user can choose to see the updated expense history.

4. `show_updated_expense_history(message, bot)`: 
If the user chooses to see the updated expense history, this function is called to display it.

5. `deleteHistory(chat_id)`: 
This function is used to delete the entire expense history for a specific user based on their `chat_id`.


# How to run this feature?
Rutuja Rashinkar, [19-10-2023 10:30 PM]
/delete_expense

My_MyDollarBot_bot, [19-10-2023 10:30 PM]
Select expense to be deleted:

Rutuja Rashinkar, [19-10-2023 10:30 PM]
Date=16-Oct-2023 20:36,  Category=Utilities,  Amount=$77.0

My_MyDollarBot_bot, [19-10-2023 10:31 PM]
Are you sure you want to delete? Y/N

Rutuja Rashinkar, [19-10-2023 10:31 PM]
y

My_MyDollarBot_bot, [19-10-2023 10:31 PM]
The following record has been deleted:

My_MyDollarBot_bot, [19-10-2023 10:31 PM]
|     DATE          |    CATEGORY       |   AMOUNT    |
+-------------------+-------------------+-------------+
| 16-Oct-2023 20:36 | Utilities         | 77.0        |
+-------------------+-------------------+-------------+

My_MyDollarBot_bot, [19-10-2023 10:31 PM]
Do you want to see the updated expense history? Y/N

Rutuja Rashinkar, [19-10-2023 10:31 PM]
y

My_MyDollarBot_bot, [19-10-2023 10:31 PM]
|     DATE          |    CATEGORY       |   AMOUNT    |
+-------------------+-------------------+-------------+
| 16-Oct-2023 18:51 | Food              | 50.0        |
| 16-Oct-2023 18:51 | Transport         | 20.0        |
| 16-Oct-2023 20:30 | Shopping          | 40.0        |
| 16-Oct-2023 20:34 | Utilities         | 65.0        |
| 19-Oct-2023 20:41 | Utilities         | 120.0       |
+-------------------+-------------------+-------------+