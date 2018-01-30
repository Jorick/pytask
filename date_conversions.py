"""Module to handle conversions of date format to several string formats."""
import datetime


def text_to_date(text_due_date):
    """Convert text like "tomorrow" into a date format."""
    text_due_date = text_due_date.lower()
    if text_due_date == "today":
        return datetime.date.today()

    elif text_due_date == "tomorrow":
        return datetime.date.today() + datetime.timedelta(days=1)

    else:
        date_list = [int(i) for i in text_due_date.split("-")]
        return datetime.date(date_list[0], date_list[1], date_list[2])


def date_to_iso(date):
    """Return a date object in string iso format."""
    return date.isoformat()


def iso_to_date(iso_date):
    """Convert a date in string iso format to Date object."""
    date_list = [int(i) for i in iso_date.split("-")]
    return datetime.date(date_list[0], date_list[1], date_list[2])


def date_to_text(due_date):
    """Convert a date in date format to readible text "tomorrow"."""
    date_diff = due_date - datetime.date.today()
    if date_diff == datetime.timedelta(days=0):
        return "Today"
    elif date_diff == datetime.timedelta(days=1):
        return "Tomorrow"
    elif date_diff == datetime.timedelta(days=2):
        return "In two days"
    elif date_diff > datetime.timedelta(days=2):
        return due_date.isoformat()
    else:
        return "Task overdue!"
