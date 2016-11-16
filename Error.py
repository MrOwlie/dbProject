

class Error:

    def __init__:
        global errors = {'', list()}

    def append(key, value):
        return errors[key].append(value)

    def get(key):
        data = errors[key]
        errors.reset(key)
        return data

    def reset(key):
        errors[key] = list()
