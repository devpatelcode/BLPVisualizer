# BLPVisualizer

Bell-LaPadula (BLP) access control simulator for Lab 5, featuring 18 test cases.

## Files

- `BLP.py` — security levels, subjects, objects, and read/write rules.
- `Cases.py` — implementation of all 18 cases.
- `ScreenshotWalkthrough.py` — step through each case for console screenshots.
- `verify_cases.py` — automated checks for all 18 cases.

## Run

Requires Python 3.8 or later. No additional packages are needed.

```bash
python3 Cases.py
```

Choose `1`–`18` to run a specific case, `A` to run all cases, or `Q` to exit.

To display each case and pause for screenshots:

```bash
python3 ScreenshotWalkthrough.py
```

To check the expected access decisions:

```bash
python3 verify_cases.py
```

Each case starts from the same initial subjects, objects, and security levels.
