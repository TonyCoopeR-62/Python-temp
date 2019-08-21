try:
    text = input('Input something')
except EOFError:
    print('Why you use EOF')
except KeyboardInterrupt:
    print('you are aborted script')
else:
    print('You are input {0}'.format(text))