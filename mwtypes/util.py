def none_or(val, func):
    if val is None:
        return None
    else:
        return func(val)
