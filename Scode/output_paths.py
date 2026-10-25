import os
from datetime import datetime

def output_paths(cfgExp):
    curr_dir = os.getcwd()
    os.chdir(curr_dir)
    os.chdir('..')

    os.sys.path.append(os.path.join(os.getcwd(), 'Experiment_Functions'))
    os.sys.path.append(os.path.join(os.getcwd(), 'Stimuli'))
    os.sys.path.append(os.path.join(os.getcwd(), 'Results'))

    cfgFile = {}
    cfgFile['res'] = os.path.join(curr_dir, 'Results')
    cfgFile['stim'] = os.path.join(os.getcwd(), 'Stimuli', 'Visual_Stimuli')
    cfgFile['cue'] = os.path.join(os.getcwd(), 'Stimuli', 'Cue_Stimuli')

    date_str = datetime.now().strftime('%Y%m%d_%H%M%S')
    cfgFile['logFile'] = f"{date_str}_sub-{cfgExp['sub']}_ses-{cfgExp['ses']}_logfile.pkl"

    os.chdir(curr_dir)

    return cfgFile
