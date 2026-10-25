from psychopy import visual, prefs, plugins
try:
    from pypixxlib import _libdpx as dp
except ImportError:
    dp = None

plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'

def initialize_datapixx_device():
    dp.DPxClose()

    print("Opening DataPixx device...")
    dp.DPxOpen()

    isReady = dp.DPxIsReady()
    if not isReady:
        raise ConnectionError('VPixx Hardware not detected! Check your connection and try again.')

    dp.DPxStopAllScheds()
    dp.DPxEnableDoutPixelModeGB()
    dp.DPxWriteRegCache()

    print("DataPixx device initialized and ready.")

def enableButtonSchedules(pulse_ms=25):    # 25 ms = 3 frames at 120 Hz (DataPixx)
    #Din0 - Red
    redWaveform = [4, 0, 0]

    #Din1 - Yellow
    yellowWaveform = [4, 0, 0]

    #Din2 - Green
    greenWaveform = [16, 0, 0]

    #Din3 - Blue
    blueWaveform = [16, 0, 0]

    redAdd = 0+4096*0
    yellowAdd = 0+4096*1
    greenAdd = 0+4096*2
    blueAdd = 0+4096*3

    #write schedules into ram
    dp.DPxWriteRam(redAdd, redWaveform)
    dp.DPxWriteRam(yellowAdd, yellowWaveform)
    dp.DPxWriteRam(greenAdd, greenWaveform)
    dp.DPxWriteRam(blueAdd, blueWaveform)

    #configure buffer-- only need to configure the first one, rest will follow the same format
    dp.DPxSetDoutBuff(redAdd, len(redWaveform)*2)
    dp.DPxSetDoutSched(0, 10, 'hz', len(redWaveform)+1)
    dp.DPxUpdateRegCache()

    #turn off debounce so button jitter is suppressed
    dp.DPxEnableDinDebounce()

    #Enable button schedules, set mode to 1 for RPx /MRI setup
    dp.DPxSetDoutButtonSchedulesMode(1)
    dp.DPxEnableDoutButtonSchedules()
    dp.DPxWriteRegCache()

    #print(f"Button schedules enabled: red -> 4, blue -> 16, {pulse_ms} ms pulse (yellow/green inactive).")

def drawPixelModeTrigger(win, pixelValue):
    rect = visual.Rect(
        win=win,
        width=10,
        height=10,
        pos=(-win.size[0]/2 + 0.5, win.size[1]/2 - 0.5),
        units='pix',
        fillColor=pixelValue,
        lineColor=pixelValue,
        colorSpace='rgb255'
    )
    rect.draw()

def Trigger2RGB(trigger):
    return [
        trigger % 256,
        (trigger >> 8) % 256,
        (trigger >> 16) % 256
    ]

# DIN log values for this response box (measured with check_buttons.py).
# 65520 (release/idle) is the same for both buttons and is excluded as a response.
buttonCodes = {65524: 'green', 65522: 'yellow'}

def read_button_press(logStatus):
    """Return the first response-button colour found in the DIN log, or None.

    Maps logged DIN values to button colours via buttonCodes (blue=65528,
    red=65521); release/idle (65520) is excluded.
    """
    if dp is None:
        return None
    data = dp.DPxReadDinLog(logStatus, logStatus['newLogFrames'])
    for entry in data:
        value = entry[1] if isinstance(entry, (list, tuple)) else entry
        colour = buttonCodes.get(value)
        if colour and colour != 'release':
            return colour
    return None
