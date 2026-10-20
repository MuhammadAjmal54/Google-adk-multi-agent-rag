# tools/general_tools.py
# General Agent ke tools - Single comprehensive tool to prevent tool-calling loops

from datetime import datetime


def get_datetime_info() -> str:
    """
    Get complete current date, time, and day information in one call.
    Returns today's date, current time, day name, whether it is a working day or weekend,
    week number, and day of year. Call this tool ONCE to answer any date or time question.

    Returns:
        A complete formatted string with all date and time details.
    """
    now = datetime.now()
    is_weekday = now.weekday() < 5  # 0=Monday, 4=Friday
    day_type = "Weekday (Working Day)" if is_weekday else "Weekend (Non-working day)"

    return (
        f"Current Date  : {now.strftime('%A, %B %d, %Y')}\n"
        f"Current Time  : {now.strftime('%I:%M:%S %p')}\n"
        f"Day           : {now.strftime('%A')}\n"
        f"Day Type      : {day_type}\n"
        f"Month         : {now.strftime('%B %Y')}\n"
        f"Day of Year   : {now.timetuple().tm_yday}\n"
        f"Week Number   : {now.isocalendar()[1]}"
    )