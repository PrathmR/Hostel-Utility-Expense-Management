def validate_usage(value):
    try:
        value = float(value)
        if value < 0:
            return False
        return True
    except:
        return False
