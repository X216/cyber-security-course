status = input('Input your status : ')

match status:
    case 'active':
        print('You are active')
    case 'Lonely':
        print('You are lonely')
    case _:
        print('Nothing found here')
