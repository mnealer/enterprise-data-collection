from datetime import datetime


def not_null(value):
    if not value:
        return False
    elif len(value) > 0:
        return True
    else:
        return False


def string_length(value, min, max):
    if not value:
        return False
    elif not isinstance(value, str):
        return False
    elif min <= len(value) <= max:
        return True
    else:
        return False


def is_string(value):
    if not isinstance(value, str):
        return False
    else:
        return True


def is_number(value):
    if not isinstance(value, int) and not isinstance(value, float):
        return False
    else:
        return True


def number_range(value, min, max):
    if not isinstance(value, int) and not isinstance(value, float):
        return False
    elif min <= value <= max:
        return True
    else:
        return False


def py_date(value):
    try:
        return datetime.strptime(value, '%Y-%m-%d')
    except ValueError:
        return False


def py_time(value):
    try:
        return datetime.strptime(value, '%H:%M:%S')
    except ValueError:
        return False


def py_datetime(value):
    datetime_obj = None
    for ft in ['%Y-%m-%d', '%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M:%S.%f']:
        try:
            datetime_obj = datetime.strptime(value, ft)
            break
        except ValueError:
            pass
    if datetime_obj:
        return datetime_obj
    else:
        return False
