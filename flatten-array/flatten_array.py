def flatten(iterable):
    return nested_list(iterable)

def nested_list(args):
    items = []
    for arg in args:
        if arg is None or arg == () or arg == {}:
            next
        elif type(arg) == list:
            items += flatten(arg)
        else:
            items.append(arg)
    return items
