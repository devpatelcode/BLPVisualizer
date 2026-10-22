# BLPVisualizer

This is my Bell-LaPadula access control lab. It has 18 cases that show when a user is allowed or denied access to a file based on its security level.

## What's included

- `BLP.py` contains the Bell-LaPadula rules and keeps track of each user and file's security level.
- `Cases.py` has all 18 lab cases.
- `ScreenshotWalkthrough.py` runs one case at a time and pauses so I can take screenshots.
- `verify_cases.py` checks that each case gives the expected result.

## Running the lab

You'll need Python 3. No extra packages are required.

```bash
python3 Cases.py
```

Enter a number from 1 to 18 to run that case, `A` to run every case, or `Q` to quit.

For screenshots, I also added a way to go through the cases one at a time:

```bash
python3 ScreenshotWalkthrough.py
```

Press Enter after capturing each case to move to the next one.

To check the expected allow/deny results:

```bash
python3 verify_cases.py
```

Each case starts with the same original subjects, files, and security levels so the results don't affect each other.
