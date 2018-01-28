import datetime


def text_to_date(text_due_date):
    """Convert text like "tomorrow" into a date format."""
    text_due_date = text_due_date.lower()
    if text_due_date == "today":
        return datetime.date.today()

    elif text_due_date == "tomorrow":
        return datetime.date.today() + datetime.timedelta(days=1)

    else:
        print("Not a valid string in text_to_date")


def date_to_text(due_date):
    """Convert a date in date format to readible text "tomorrow"."""
    date_today = datetime.date.today()
    date_diff = due_date - date_today
    if date_diff == date_today():
        return "Today"
    elif date_diff == datetime.timedelta(days=1):
        return "Tomorrow"
    elif date_diff == datetime.timedelta(days=2):
        return "In two days"
    elif date_diff > datetime.timedelta(days=2):
        pass
    else:
        return "Task overdue!"
