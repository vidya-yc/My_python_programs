
def is_sorted(t):
    for index, item in enumerate(t):
        try:
            if item > t[index + 1]:
                return False
        except IndexError:
            return True
