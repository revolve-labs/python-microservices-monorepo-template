from datetime import datetime, timezone


def utcnow() -> datetime:
    """Generates timezone-aware UTC datetime."""
    return datetime.now(timezone.utc)


def parse_date(date_to_be_parsed: str) -> datetime:
    datetime_obj = datetime.fromisoformat(
        date_to_be_parsed
    )  # Parses from ISO format
    if datetime_obj.tzinfo is None:  # If no timezone present
        datetime_obj = datetime_obj.replace(tzinfo=timezone.utc)
    elif (
        datetime_obj.tzinfo != timezone.utc
    ):  # If some other timezone besides UTC present
        datetime_obj = datetime_obj.astimezone(timezone.utc)
    return datetime_obj
