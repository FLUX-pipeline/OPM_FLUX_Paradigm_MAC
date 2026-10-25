from psychopy import visual, core, event

win = visual.Window(size=(900, 600), color='black', fullscr=False, units='norm')

screens = [
    "Screen 1 of 3\n\nPress Y to continue",
    "Screen 2 of 3\n\nPress Y to continue",
    "Screen 3 of 3\n\nPress Y to finish",
]

for i, txt in enumerate(screens):
    stim = visual.TextStim(win, text=txt, color='white')
    stim.draw()
    win.flip()

    keys = event.waitKeys(keyList=['y'])
    print(f"Screen {i + 1}: got key press {keys}", flush=True)

    confirm = visual.TextStim(win, text="Key detected!", color='green')
    confirm.draw()
    win.flip()
    core.wait(0.5)

win.close()
core.quit()
