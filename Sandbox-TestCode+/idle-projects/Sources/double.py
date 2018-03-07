def get_random_name():
    from random import choice
    name_list = ['RAE', 'RYLEE', 'JOSH', 'BRIAN', 'DAVE']
    return choice(name_list), choice(name_list)
