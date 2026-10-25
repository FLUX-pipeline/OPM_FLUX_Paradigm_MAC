from psychopy.hardware import keyboard

def keyboard_setup(cfgExp):
    cfgExp['kbresp']=['y']
    cfgExp['kbresp_no']=['n']
    cfgExp['kbresp_quit']=['s']
    cfgExp['quitKey'] = 'white'
    cfgExp['noKey'] = 'yellow'
    cfgExp['yesKey'] = 'blue'
    cfgExp['respKey'] = 'blue'

    cfgExp['activeKeys'] = [cfgExp['quitKey'], cfgExp['respKey'], cfgExp['yesKey'], cfgExp['noKey']]

    cfgExp['kb'] = keyboard.Keyboard()
    cfgExp['kb'].start()

    cfgExp['kb'].clearEvents()

    return cfgExp
