from datetime import datetime


def datetime_to_iso(dt: datetime) -> str:
    return dt.isoformat()
