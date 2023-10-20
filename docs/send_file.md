# About DollarSplitBot's /add Feature
#TO-DO
This feature enables the user to send email to registered users about the owings.

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/shonilbhide/dollar_bot/blob/main/code/send_mail.py)

# Code Description
## Functions

- run(message, bot):
This function is the entry point of the program. It asks the user to provide an email address.
It is meant to be called when the program starts.
It registers a callback to handle the user's response by calling add_emails.

- add_emails(message, bot):
This function is called after the user provides an email address.
It stores the user's email address in a dictionary (user_emails) with their chat ID as the key.
It can also validate the email address to ensure it's in the correct format.
It asks the user whether they want to send an email to the provided address.
If the user responds "Y" or "y", it calls the send_email function.

- is_valid_email(email):
This function checks if an email address is in a valid format using a regular expression.
It helps ensure that the email provided by the user is correctly formatted.

- send_email(choice, bot):
This function sends email notifications to the addresses stored in the user_emails dictionary.
It uses Gmail's SMTP server to send the emails.
It composes an email message with a subject and body, where the body contains calculated data from helper.read_json().
It iterates through the user_emails dictionary, sending an email to each address.
Finally, it closes the SMTP connection.

- format_text_data(user_list):
This function takes a user list, likely with financial data, and formats it into a string.
The formatted data is enclosed in triple backticks (```) for a code-like appearance.
It iterates through the user list, presenting information about who owes money and to whom.

# How to run this feature?
Once the project is running(please follow the instructions given in the main README.md for this), please type /send_email into the telegram bot.
