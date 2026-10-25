import os

from psychopy import core, visual

from abort import AbortExperiment, check_abort
from psychopy_prefs import psychopy_prefs
from screen_setup import screen_setup
from datapixx import initialize_datapixx_device, enableButtonSchedules
from show_feedback import show_feedback
from save_and_quit import save_and_quit
from output_paths import output_paths
from display_cue import display_cue
from display_fixation_dot import display_fixation_dot
from display_visual_stim import display_visual_stim
from show_text_screen import show_text_screen
from experiment_config import experiment_config
from screen_config import screen_config
from stim_config import stim_config
from timing_config import timing_config
from trigger_config import trigger_config
from prepare_stimuli import prepare_stimuli
from keyboard_setup import keyboard_setup
from participant_dialog import participant_dialog
from load_stimuli import load_stimuli
from show_instructions import show_instructions
from duration_to_frames import duration_to_frames
from instruction_text import instruction_text

os.system('cls' if os.name == 'nt' else 'clear')

psychopy_prefs()
cfgExp = participant_dialog()
cfgFile = output_paths(cfgExp)

cfgExp, cfgOutput = experiment_config(cfgExp)
cfgExp = timing_config(cfgExp)
cfgTrigger = trigger_config()
cfgStim = stim_config()
cfgScreen = screen_config(cfgExp)

win = visual.Window(
    color=cfgScreen['backgroundColor'],
    fullscr=1,
    units='deg',
    screen=cfgScreen['screenNumber'],
    monitor=cfgExp['monitor']
)
win.winHandle.activate()  # force OS keyboard focus onto the stimulus window (needed when launched from Runner/Coder on macOS)

if os.name != 'nt':
    # On macOS, activating the pyglet window alone is not enough: the OS still
    # routes keystrokes to whichever *application* is frontmost, which stays
    # PsychoPy Studio/Runner (the launcher) unless we explicitly activate this
    # process. Without this, no key presses reach the experiment at all.
    try:
        from AppKit import NSApplication, NSApp
        NSApplication.sharedApplication()
        NSApp.activateIgnoringOtherApps_(True)
    except ImportError:
        pass

cfgScreen['window'] = win

cfgStim, cfgExp, cfgTrigger = load_stimuli(cfgFile, cfgExp, cfgStim, cfgTrigger,cfgScreen)

cfgTxt = instruction_text()

cfgScreen = screen_setup(cfgScreen)

cfgExp = duration_to_frames(cfgExp, cfgScreen)
presentingStr = prepare_stimuli(cfgScreen, cfgStim, cfgExp)
if not cfgExp['local']:
    initialize_datapixx_device()
    enableButtonSchedules()

cfgExp = keyboard_setup(cfgExp)
cfgScreen['vbl'] = win.flip()
cfgOutput['vbl'] = cfgScreen['vbl']

show_instructions(cfgScreen, cfgTxt, cfgExp, presentingStr, cfgStim,cfgTrigger,cfgOutput)

cfgOutput = show_text_screen(cfgScreen, cfgExp, cfgTxt['startTxt'], cfgTxt, cfgOutput, cfgTrigger, cfgFile, cfgStim)

nstim = -1

try:
    for blk in range(0, cfgExp['numBlock']):
        block_text = f"Block {blk + 1} out of {cfgExp['numBlock']}"
        text_stim = visual.TextStim(cfgScreen['window'], text=block_text, color='white')
        text_stim.draw()
        cfgScreen['window'].flip()
        cfgOutput['blkStrtTmPnt'][blk] = core.getTime()
        core.wait(2)

        for trl in range(0, cfgExp['numTrial']):
            check_abort()

            nstim += 1

            cfgOutput['trlStrtTmPnt'][nstim] = core.getTime()

            cfgOutput = display_fixation_dot(cfgScreen, cfgExp, cfgStim, nstim, 1, cfgOutput)

            cfgOutput = display_cue(cfgScreen, presentingStr, nstim, cfgStim, cfgExp, cfgTrigger, cfgOutput)

            cfgOutput = display_fixation_dot(cfgScreen, cfgExp, cfgStim, nstim, 0, cfgOutput)

            cfgOutput = display_visual_stim(presentingStr, nstim, cfgScreen, cfgExp, cfgOutput, cfgStim, cfgTrigger,cfgTxt,cfgFile)

        cfgOutput = show_feedback(cfgOutput, cfgExp, nstim, blk, cfgScreen, cfgTrigger)
        if blk != cfgExp['numBlock']:
            cfgOutput = show_text_screen(cfgScreen, cfgExp, cfgTxt['breakTxt'], cfgTxt, cfgOutput, cfgTrigger, cfgFile, cfgStim)

    cfgOutput = show_text_screen(cfgScreen, cfgExp, cfgTxt['endTxt'], cfgTxt, cfgOutput, cfgTrigger, cfgFile, cfgStim)
    cfgOutput = save_and_quit(cfgFile, cfgExp, cfgScreen, cfgOutput, cfgTrigger, cfgTxt, cfgStim)
except AbortExperiment:
    print('Experiment aborted by operator (x key).')
    cfgOutput = save_and_quit(cfgFile, cfgExp, cfgScreen, cfgOutput, cfgTrigger, cfgTxt, cfgStim)
