from datetime import datetime, timedelta


def get_day_and_check_next_month(days: int):
    current_date = datetime.now()

    future_date = current_date + timedelta(days)

    is_next_month = current_date.month != future_date.month

    return future_date.day, is_next_month
