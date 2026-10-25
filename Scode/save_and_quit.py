import os
import pickle
from psychopy import core, logging

def save_and_quit(cfgFile, cfgExp, cfgScreen, cfgOutput, cfgTrigger, cfgTxt, cfgStim):
    cfgScreen['window'].flip()
    cfgOutput['endTmPnt'] = core.getTime()

    cfgScreen['window'].close()

    log_file_path = os.path.join(cfgFile['res'], cfgFile['logFile'])

    log_dir = os.path.dirname(log_file_path)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
        logging.info(f'Created directory for log file at {log_dir}')

    if os.path.exists(log_file_path):
        logging.warning('Log file will be overwritten!')
        cont = input('Do you want to continue? (y/n) ').strip().lower()
        while True:
            if cont == 'y':
                break
            elif cont == 'n':
                raise Exception('Experiment aborted by operator.')
            else:
                cont = input('Invalid input. Do you want to continue? (y/n) ').strip().lower()

    # Complete record: pickle the full cfgOutput (lossless, all arrays / types).
    with open(log_file_path, 'wb') as file:
        pickle.dump(cfgOutput, file)

    # Human-readable per-trial table (.csv) for quick viewing / analysis (opens in
    # Excel, R, MATLAB, etc.). The pickle above stays the complete backup; if this
    # export fails the run is unaffected. pandas is imported here so the experiment
    # never depends on it.
    try:
        import pandas as pd
        n = cfgExp['numStim']
        trials = pd.DataFrame({
            'trial': range(1, n + 1),
            'cued_side': cfgExp['cuesDir'],          # Right / Left
            'target_present': cfgExp['corrResp'],    # 1 = target, 0 = catch
            'letter': cfgExp['letter'],              # T / L / '' (catch)
            'required_button': cfgExp['corrButton'], # blue (T) / red (L)
            'pressed_button': cfgOutput['pressedButton'],
            'responded': cfgOutput['presd'],         # 2 = pressed, 0 = no response
            'correct': cfgOutput['correct'],
            'RT_from_target_s': cfgOutput['RT_trig'],
            'RT_from_resp_start_s': cfgOutput['RT_KbQueue'],
            'trial_start_s': cfgOutput['trlStrtTmPnt'],
            'cue_onset_s': cfgOutput['cueOnTmPnt'],
            'stim_onset_s': cfgOutput['stmOnTmPnt'],
            'target_onset_s': cfgOutput['targetOnTmPnt'],
            'response_time_s': cfgOutput['respTmPnt'],
        })
        trials.to_csv(log_file_path.replace('.pkl', '.csv'), index=False)
    except Exception as e:
        logging.warning(f'Could not write CSV trial table: {e}')

    core.quit()

    return cfgOutput
