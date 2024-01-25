def validate(val):

    try:
        val = float(val)
    except ValueError:
        return False

    if val < 0:
        return False
    return True

def area_of_triangle(base, height):
    if validate(base) and validate(height):
        return (1/2 * float(base) * float(height))

