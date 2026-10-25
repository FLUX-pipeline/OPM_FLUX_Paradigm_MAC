def trigger_config():
    cfgTrigger = {
        'stimOnset': 1024,
        'reston': 256,
        'restoff': 1024,
        # cue-onset codes per cued side
        'cueRight': 256,
        'cueLeft': 4096,
        # target (letter) onset codes per side
        'targetRight': 16384,
        'targetLeft': 65536,
    }
    return cfgTrigger
