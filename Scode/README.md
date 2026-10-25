# Spatial Attention — Letter (T / L) Discrimination Task

A simple visual attention experiment. Two moving gratings appear on the left and
right. An arrow tells you which side to pay attention to. A letter (**T** or **L**)
then briefly appears on the attended grating, and you press the matching button.

It can run two ways:
- **Lab** — on the rig with the VPixx hardware and the coloured response buttons.
- **Local** — on any laptop (no special hardware) using the keyboard, for testing/practice.

---

## How to start

1. Open a terminal in this folder.
2. Run:

   ```
   python run_experiment.py
   ```

3. A small window appears. Fill in:
   - **Subject Code** (e.g. `S123`)
   - **Session** (e.g. `01`)
   - **Run location** — choose **`lab`** or **`local`**
4. Click **OK**.

---

## What you do during the task

1. An instruction screen appears. Read it, then press **`Y`** to continue to the next one.
2. Keep your eyes on the small dot in the centre of the screen the whole time.
3. An **arrow** points **left** or **right** — pay attention to that side (without moving your eyes).
4. Two moving gratings appear. A letter (**T** or **L**) flashes on the side the arrow pointed to.
5. **Press the matching button as quickly and accurately as you can** (see below).
6. On some trials no letter appears — just do nothing and wait for the next trial.

---

## Which button to press

### 🧪 Lab setup (VPixx response buttons)

| You see | Press |
|---------|-------|
| **T** | the **BLUE** button |
| **L** | the **RED** button |

### 💻 Local setup (laptop keyboard)

| You see | Press |
|---------|-------|
| **T** | the **`B`** key  (B = blue) |
| **L** | the **`R`** key  (R = red) |

---

## Other keys (both setups)

| Key | What it does |
|-----|--------------|
| **`Y`** | Continue / start / move past an instruction or break screen |
| **`X`** | Stop the experiment immediately (your data so far is saved) |

> Tip: `B` = **B**lue = **T**, `R` = **R**ed = **L**.

---

## Where the data goes

When the experiment finishes (or you press `X`), the results are saved automatically
into the **`Results/`** folder as a `.pkl` file named with the date, subject code and
session, for example:

```
Results/20260620_143052_sub-S123_ses-01_logfile.pkl
```

---

## Notes for the experimenter

- **Local mode needs no hardware** — `pypixxlib` is optional; the VPixx device, button
  schedules and button logging are all skipped automatically when you choose `local`.
- All adjustable settings live in clearly named files:
  - `screen_config.py` — monitor / display settings
  - `stim_config.py` — stimulus sizes, colours, positions
  - `timing_config.py` — trial durations
  - `trigger_config.py` — trigger codes
  - `experiment_config.py` — number of blocks / trials (`numTrial`)
- The T/L counts are split 50/50 automatically based on the number of trials.
