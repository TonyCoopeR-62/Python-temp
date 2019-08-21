while True:
    s = input('write something-')
    if s == 'ex':
        break
    if len(s) < 3:
        print('bigger')
        continue
    print('its ok')