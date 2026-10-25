from psychopy import gui, core

def participant_dialog():
    info = {
        'Subject Code': 'S123',
        'Session': '01',
        'Run location': ['lab', 'local']
    }

    dlg = gui.DlgFromDict(dictionary=info, title='Experiment Details', sortKeys=False)

    if not dlg.OK:
        core.quit()

    cfgExp = {
        'sub': info['Subject Code'],
        'ses': info['Session'],
        'local': info['Run location'] == 'local'
    }

    return cfgExp
