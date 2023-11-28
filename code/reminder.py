import schedule
import threading
import time
import helper

# Define a dictionary to store scheduled jobs
scheduled_jobs = {}
stop_schedule_thread = {}    # False





# Function to send reminders
def send_reminder(chat_id, reminder_message, bot):
    bot.send_message(chat_id, f"Reminder: {reminder_message}")

# Function to schedule a reminder job
def schedule_reminder(chat_id, reminder_message, bot):
    # Schedule the job for checking and sending reminders every 1 minute

    global stop_schedule_thread
    stop_schedule_thread[chat_id] = False    # False

    
    # job = schedule.every(1).minutes.do(send_reminder, chat_id, reminder_message, bot)
    job = schedule.every(1).minutes.do(set_reminder, chat_id, bot)

    # Store the job in the scheduled_jobs dictionary
    scheduled_jobs[chat_id] = job
    print(scheduled_jobs)
    print(reminder_message)

    # Start the scheduler in a separate thread
    schedule_thread = threading.Thread(target=schedule_job, args=(chat_id,))
    schedule_thread.start()

# Function to cancel a scheduled reminder
def cancel_reminder(chat_id, bot):
    # Check if the job is in the dictionary
    global stop_schedule_thread
    if chat_id in scheduled_jobs:
        # Manually remove the job from the dictionary
        removed_job = scheduled_jobs.pop(chat_id, None)
        print(scheduled_jobs)
        
        if removed_job:
            stop_schedule_thread[chat_id] = True
            #removed_job.schedule_removal()  # This should cancel the job
            print(f"Reminder cancelled for chat_id: {chat_id}")
        else:
            print(f"Error: Unable to remove reminder for chat_id: {chat_id}")
    else:
        print(f"No active reminder found for chat_id: {chat_id}")

# Function to run the scheduler
def schedule_job(chat_id):
    global stop_schedule_thread
    while not stop_schedule_thread.get(chat_id, False):
        schedule.run_pending()
        time.sleep(1)

# Function to check for dues and set reminders
def set_reminder(chat_id, bot):
    if chat_id not in scheduled_jobs:
        print(f"Reminder for chat_id {chat_id} already cancelled.")
        return


    # Load user data
    user_data = helper.read_json()

    # Get user details
    user_details = user_data.get(str(chat_id), {})

    dues_exist = any(owed_amount > 0 for owed_amount in user_details.get("owed", {}).values())

    if dues_exist:
        # Compose a detailed reminder message
        detailed_reminder = "Reminder! "
        for creditor, amount in user_details.get("owed", {}).items():
            if amount > 0:
                detailed_reminder += f"You owe {creditor} ${amount}. "

        print(detailed_reminder)
        # Set the reminder and schedule it
        bot.send_message(chat_id, detailed_reminder)
    else:
        bot.send_message(chat_id, "No reminders set. No dues to settle.")