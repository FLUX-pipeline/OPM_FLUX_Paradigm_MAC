"""Standalone trigger test: press a key, send the matching trigger value.

Uses the same PixelMode-GB path as the experiment (datapixx.py + trigger_config.py),
so whatever lands on the recording here is exactly what the task will send.

Keys:
    1 = stimOnset      2 = cueRight     3 = cueLeft
    4 = targetRight    5 = targetLeft
    esc = quit
"""
from psychopy import visual, core, event
from datapixx import initialize_datapixx_device, drawPixelModeTrigger, Trigger2RGB
from trigger_config import trigger_config

TRIGGER_FRAMES = 3            # frames the trigger pixel stays on (~25 ms at 120 Hz)
SCREEN_NUMBER  = 1            # DataPixx display (2nd screen in the lab; use 0 if testing locally)

cfgTrigger = trigger_config()
keyTrigger = {
    '1': ('stimOnset',   cfgTrigger['stimOnset']),
    '2': ('cueRight',    cfgTrigger['cueRight']),
    '3': ('cueLeft',     cfgTrigger['cueLeft']),
    '4': ('targetRight', cfgTrigger['targetRight']),
    '5': ('targetLeft',  cfgTrigger['targetLeft']),
}

initialize_datapixx_device()          # enables PixelMode GB (dout 8-23)

win = visual.Window(fullscr=True, screen=SCREEN_NUMBER, units='pix', color='black')

info = ('Press 1-5 to send a trigger, Esc to quit.\n\n'
        '1=stimOnset  2=cueRight  3=cueLeft  4=targetRight  5=targetLeft')
msg = visual.TextStim(win, text=info, color='white', height=24)
status = visual.TextStim(win, text='', color='yellow', height=28, pos=(0, -200))

msg.draw()
win.flip()

running = True
while running:
    for k in event.getKeys():
        if k in ('escape', 'q'):
            running = False
            break
        if k in keyTrigger:
            name, code = keyTrigger[k]
            print(f'Sending {name} = {code}  (RGB={Trigger2RGB(code)})')
            # Hold the trigger pixel for a few frames so the recording samples it.
            for _ in range(TRIGGER_FRAMES):
                msg.draw()
                status.text = f'{name} = {code}'
                status.draw()
                drawPixelModeTrigger(win, Trigger2RGB(code))
                win.flip()
            # Clear the trigger pixel back to 0 (no drawPixelModeTrigger this flip).
            msg.draw()
            status.draw()
            win.flip()

win.close()
core.quit()
