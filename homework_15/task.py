import math


def format_duration(seconds):
    units = [("year", 31536000), ("day", 86400), ("hour", 3600), ("minute", 60), ("second", 1)]
    result = []

    if seconds == 0:
        return "now"

    for unit_name, unit_duration in units:
        if seconds >= unit_duration:
            num_units = seconds // unit_duration
            seconds %= unit_duration
            unit_name += "s" if num_units > 1 else ""
            result.append(f"{num_units} {unit_name}")

    return ", ".join(result[:-1]) + " and " + result[-1] if len(result) > 1 else result[0]





