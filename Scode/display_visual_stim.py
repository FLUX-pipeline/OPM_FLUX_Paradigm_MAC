from psychopy import visual, core, event
from datapixx import drawPixelModeTrigger, Trigger2RGB, read_button_press
from abort import check_abort
try:
    from pypixxlib._libdpx import DPxOpen, DPxUpdateRegCache, DPxStopDinLog
    from pypixxlib._libdpx import DPxSetDinLog, DPxStartDinLog, DPxGetDinStatus, DPxEnableDinDebounce
except ImportError:
    def DPxOpen(*a, **k): pass
    def DPxUpdateRegCache(*a, **k): pass
    def DPxStopDinLog(*a, **k): pass
    def DPxStartDinLog(*a, **k): pass
    def DPxEnableDinDebounce(*a, **k): pass
    def DPxGetDinStatus(*a, **k): pass
    def DPxSetDinLog(*a, **k): return {'newLogFrames': 0}

#respKeys = {'b': 'blue', 'r': 'red'}
respKeys = {'g': 'green', 'y': 'yellow'}
def display_visual_stim(presentingStr, nstim, cfgScreen, cfgExp, cfgOutput, cfgStim, cfgTrigger,cfgTxt,cfgFile):

    local = cfgExp['local']
    destvecRL=[cfgStim['destVisStimR'],cfgStim['destVisStimL']]
    cued_pos = destvecRL[0] if cfgStim['cueRndIdx'][nstim] == 1 else destvecRL[1]
    # Hard-coded target (letter) onset trigger codes (1 = Right, 2 = Left); see trigger_config.py.
    target_trigger = 16384 if cfgStim['cueRndIdx'][nstim] == 1 else 65536
    # Hard-coded stimulus (grating) onset trigger code; see trigger_config.py.
    stim_onset_trigger = 1024

    win=cfgScreen['window']
    vbl =  cfgScreen['vbl']

    fix_dot_big = visual.Circle(win, radius=cfgStim['fixBigSize'], fillColor=cfgStim['fixBigColor'], colorSpace='rgb', pos=cfgStim['fixPos'],units='deg')
    fix_dot_small = visual.Circle(win, radius=cfgStim['fixSmallSize'], fillColor=cfgStim['fixSmallColor'], colorSpace='rgb', pos=cfgStim['fixPos'],units='deg')

    # Small circle at the centre of each grating, shown for the whole trial.
    marker_R = visual.Circle(win, radius=cfgStim['markerRadius'], fillColor=cfgStim['markerColor'], lineColor=cfgStim['markerColor'], colorSpace='rgb', pos=cfgStim['destVisStimR'], units='deg')
    marker_L = visual.Circle(win, radius=cfgStim['markerRadius'], fillColor=cfgStim['markerColor'], lineColor=cfgStim['markerColor'], colorSpace='rgb', pos=cfgStim['destVisStimL'], units='deg')
    # Target letter (T/L), drawn over the circle on the cued grating during the target window.
    letter_stim = visual.TextStim(win, text=cfgExp['letter'][nstim], color=cfgStim['letterColor'], height=cfgStim['letterSize'], bold=cfgStim['letterBold'], pos=cued_pos, units='deg')

    if cfgExp['corrResp'][nstim]:
        for frm in range(cfgExp['stimFrm'][nstim]):
            check_abort()
            presentingStr['visStimR'][nstim][frm].draw()
            presentingStr['visStimL'][nstim][frm].draw()
            fix_dot_big.draw()
            fix_dot_small.draw()
            marker_R.draw()
            marker_L.draw()
            if frm == 0 or frm == 1 or frm==2:
                drawPixelModeTrigger(win, Trigger2RGB(stim_onset_trigger))
            win.flip()
            if frm == 0:
                cfgOutput['stmOnTmPnt'][nstim] = core.getTime()

        logStatus = {'newLogFrames': 0}
        if not local:
            DPxOpen()
            logStatus = DPxSetDinLog(0, 1000)   # base addr past button-schedule RAM (0..12288)
            DPxEnableDinDebounce()
            DPxStartDinLog()
            DPxUpdateRegCache()

        for frmTarget in range(cfgExp['stimFrm'][nstim], cfgExp['stimFrm'][nstim] + cfgExp['targetFrm']):
            check_abort()
            presentingStr['visStimR'][nstim][frmTarget].draw()
            presentingStr['visStimL'][nstim][frmTarget].draw()
            fix_dot_big.draw()
            fix_dot_small.draw()
            marker_R.draw()
            marker_L.draw()
            letter_stim.draw()
            if cfgExp['stimFrm'][nstim] <= frmTarget < cfgExp['stimFrm'][nstim] + 3:
                drawPixelModeTrigger(win, Trigger2RGB(target_trigger))
            win.flip()
            if frmTarget == cfgExp['stimFrm'][nstim]:
                cfgOutput['targetOnTmPnt'][nstim] = core.getTime()

        cfgOutput['respStartTime'][nstim] = core.getTime()
        if local:
            event.getKeys(keyList=list(respKeys))
        for frame_count in range((cfgExp['stimFrm'][nstim] + cfgExp['targetFrm']), max(int(cfgExp['overFrm'][nstim]), int(cfgExp['tFrame']))):
            check_abort()
            if frame_count < cfgExp['overFrm'][nstim]:
                presentingStr['visStimR'][nstim][frame_count].draw()
                presentingStr['visStimL'][nstim][frame_count].draw()
                fix_dot_big.draw()
                fix_dot_small.draw()
                marker_R.draw()
                marker_L.draw()
                cfgScreen['window'].flip()
            else:
                fix_dot_big.draw()
                fix_dot_small.draw()
                cfgScreen['window'].flip()
            if not local:
                DPxUpdateRegCache()
                DPxGetDinStatus(logStatus)
                pressed = read_button_press(logStatus) if logStatus['newLogFrames'] > 0 else None
            else:
                keys = event.getKeys(keyList=list(respKeys))
                pressed = respKeys.get(keys[0]) if keys else None
            detected = pressed is not None
            if detected:
                cfgOutput['respTmPnt'][nstim] = core.getTime()
                cfgOutput['respTmKbQueue'][nstim] = cfgOutput['respTmPnt'][nstim]
                cfgOutput['presd'][nstim] = 2
                cfgOutput['pressedButton'][nstim] = pressed if pressed else ''
                cfgOutput['correct'][nstim] = 1 if pressed == cfgExp['corrButton'][nstim] else 0
                cfgOutput['RT_KbQueue'][nstim] = cfgOutput['respTmPnt'][nstim] - cfgOutput['respStartTime'][nstim]
                cfgOutput['RT_trig'][nstim] = cfgOutput['respTmPnt'][nstim] - cfgOutput['targetOnTmPnt'][nstim]
                print(f'Response: {pressed} (required {cfgExp["corrButton"][nstim]}), correct={cfgOutput["correct"][nstim]}')
                break
        if not local:
            DPxStopDinLog()

    else:
        for frm in range(cfgExp['stimFrm'][nstim] + cfgExp['targetFrm']):
            check_abort()
            presentingStr['visStimR'][nstim][frm].draw()
            presentingStr['visStimL'][nstim][frm].draw()
            fix_dot_big.draw()
            fix_dot_small.draw()
            marker_R.draw()
            marker_L.draw()
            if frm == 0 or frm==1 or frm==2:
                drawPixelModeTrigger(win, Trigger2RGB(stim_onset_trigger))
            cfgScreen['window'].flip()
            if frm == 0:
                cfgOutput['catchOnTmPnt'][nstim] = core.getTime()

        logStatus = {'newLogFrames': 0}
        if not local:
            DPxOpen()
            logStatus = DPxSetDinLog(0, 1000)   # base addr past button-schedule RAM (0..12288)
            DPxEnableDinDebounce()
            DPxStartDinLog()
            DPxUpdateRegCache()

        cfgOutput['respStartTime'][nstim] = core.getTime()
        if local:
            event.getKeys(keyList=list(respKeys))
        for frame_count in range((cfgExp['stimFrm'][nstim] + cfgExp['targetFrm']), max(int(cfgExp['overFrm'][nstim]), int(cfgExp['tFrame']))):
            check_abort()
            if frame_count < cfgExp['overFrm'][nstim]:
                presentingStr['visStimR'][nstim][frame_count].draw()
                presentingStr['visStimL'][nstim][frame_count].draw()
                fix_dot_big.draw()
                fix_dot_small.draw()
                marker_R.draw()
                marker_L.draw()
                win.flip()
            else:
                fix_dot_big.draw()
                fix_dot_small.draw()
                cfgScreen['window'].flip()
            if not local:
                DPxUpdateRegCache()
                DPxGetDinStatus(logStatus)
                pressed = read_button_press(logStatus) if logStatus['newLogFrames'] > 0 else None
            else:
                keys = event.getKeys(keyList=list(respKeys))
                pressed = respKeys.get(keys[0]) if keys else None
            detected = pressed is not None
            if detected:
                cfgOutput['respTmPnt'][nstim] = core.getTime()
                cfgOutput['respTmKbQueue'][nstim] = cfgOutput['respTmPnt'][nstim]
                cfgOutput['presd'][nstim] = 2
                cfgOutput['pressedButton'][nstim] = pressed if pressed else ''
                cfgOutput['correct'][nstim] = 0
                cfgOutput['RT_KbQueue'][nstim] = cfgOutput['respTmPnt'][nstim] - cfgOutput['respStartTime'][nstim]
                print(f'Response (catch trial - false alarm): {pressed}')
                break
        if not local:
            DPxStopDinLog()

    return cfgOutput
