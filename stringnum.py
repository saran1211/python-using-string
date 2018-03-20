def is_num(a):
    try:
        float(a)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(a)
        return True
    except (TypeError, ValueError):
        pass
 
        return False

print('The given input is:')
print(is_num('1a2b'))
