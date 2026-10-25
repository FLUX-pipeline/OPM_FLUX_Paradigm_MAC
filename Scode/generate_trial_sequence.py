import numpy as np

def generate_trial_sequence(cfgExp):
 
    catch_percentage = 10
    num_catch_trials_per_block = int(cfgExp['numTrial'] * catch_percentage / 100)
    catch_trials_per_value = num_catch_trials_per_block // 2

    original_arrays = []
    binary_arrays = []

    for _ in range(cfgExp['numBlock']):
        n_right = cfgExp['numTrial'] // 2
        n_left = cfgExp['numTrial'] - n_right   # odd extra goes here, so length == numTrial
        original_array = np.concatenate([
            np.full(n_right, 1),
            np.full(n_left, 2)
        ])
        np.random.shuffle(original_array)
        original_arrays.append(original_array.copy())

        indices_ones = np.where(original_array == 1)[0]
        indices_twos = np.where(original_array == 2)[0]

        selected_indices_ones = np.random.choice(indices_ones, catch_trials_per_value, replace=False)
        selected_indices_twos = np.random.choice(indices_twos, catch_trials_per_value, replace=False)

        catch_trial_indices = np.concatenate([selected_indices_ones, selected_indices_twos])

        modified_array = original_array.copy()
        modified_array[catch_trial_indices] = 0

        binary_arrays.append(np.where(modified_array != 0, 1, 0))

    original_array_flattened = np.array(original_arrays).flatten()
    binary_array_flattened = np.array(binary_arrays).flatten()

    cfgExp['corrResp'] = binary_array_flattened
    cfgExp['cueRndIdx'] = original_array_flattened

    # Assign a target letter to each non-catch (target-present) trial, balanced
    # 50/50 between T and L. Mapping: T -> blue button, L -> red button.
    cfgExp['letter'] = np.array([''] * cfgExp['numStim'], dtype=object)
    cfgExp['corrButton'] = np.array([''] * cfgExp['numStim'], dtype=object)
    target_idx = np.where(binary_array_flattened == 1)[0]
    n_target = len(target_idx)
    n_T = n_target // 2
    labels = np.array(['T'] * n_T + ['L'] * (n_target - n_T))
    np.random.shuffle(labels)
    cfgExp['letter'][target_idx] = labels
    cfgExp['corrButton'][target_idx] = np.where(labels == 'L', 'green', 'yellow')

    return cfgExp
