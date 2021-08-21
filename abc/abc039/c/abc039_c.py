s = input()

keyboard = 'WBWBWWBWBWBW' * 4
doremi = ['Do', '', 'Re', '', 'Mi', 'Fa', '', 'So', '', 'La', '', 'Si']
index = keyboard.find(s)

print(doremi[index])
