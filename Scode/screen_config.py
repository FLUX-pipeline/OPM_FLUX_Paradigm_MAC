from psychopy import monitors

def screen_config(cfgExp):

    cfgScreen = {}

    cfgScreen['distance'] = 65                           # viewing distance (cm)
    cfgScreen['dispSize'] = {'width': 65, 'height': 34}  # physical screen size (cm)
    cfgScreen['resolution'] = [1920, 1080]               # pixels
    cfgScreen['screenNumber'] = 0 if cfgExp['local'] else 1   # local: laptop primary (0); lab: DataPixx = 2nd screen in extended mode
    cfgScreen['white'] = [255, 255, 255]                 # text colour
    cfgScreen['backgroundColor'] = 'black'
    cfgScreen['fntSize'] = 60

    monitor = monitors.Monitor(name='testMonitor', width=cfgScreen['dispSize']['width'], distance=cfgScreen['distance'])
    monitor.setSizePix(cfgScreen['resolution'])
    monitor.save()
    cfgExp['monitor'] = monitor

    return cfgScreen
