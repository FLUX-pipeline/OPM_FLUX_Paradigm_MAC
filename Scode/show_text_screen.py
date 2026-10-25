from psychopy import visual, event, core
from save_and_quit import save_and_quit

def show_text_screen(cfgScreen, cfgExp, text, cfgTxt, cfgOutput, cfgTrigger, cfgFile, cfgStim):

    win = cfgScreen['window']
    
    win.flip()
    message = visual.TextStim(win, text=text, color=cfgScreen['white'], pos=(0, 0))
    message.draw()
    win.flip()

    notWaiting = False
    while not notWaiting:
        keys = event.waitKeys()

        if any(key in cfgExp['kbresp'] for key in keys):
            notWaiting = True
        elif any(key in cfgExp['kbresp_no'] for key in keys) or any(key in cfgExp['kbresp_quit'] for key in keys):
            win.flip()
            quit_message = visual.TextStim(win, text=cfgTxt['quitTxt'], color=[1, 1, 1], colorSpace='rgb', pos=(0, 0),units='deg')
            quit_message.draw()
            win.flip()

            abrt_keys = event.waitKeys()

            if 'y' in abrt_keys:

                cfgOutput = save_and_quit(cfgFile, cfgExp, cfgScreen, cfgOutput, cfgTrigger, cfgTxt, cfgStim)

                break
        
        event.clearEvents()
        core.wait(0.5)

    return cfgOutput
