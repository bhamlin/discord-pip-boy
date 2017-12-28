
def game_opt(user, command_line):
    args = None
    if ' ' in command_line:
        pivot = command_line.find(' ')
        command, args = command_line[:pivot], command_line[pivot+1:]
    else:
        command = command_line
    print(user, command, args)

    if command == 'i' or command == 'import':
        pass

    return 'Unknown'
