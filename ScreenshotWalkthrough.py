"""Run Lab 5 cases one at a time, pausing for manual screenshots.

Usage: python3 ScreenshotWalkthrough.py
       python3 ScreenshotWalkthrough.py --case 8
"""
import argparse
from Cases import TEST_CASES, setup_initial_state, execute_commands


def show_case(number):
    print("\033[2J\033[H", end="")
    print(f"\n================ CASE #{number} ================")
    blp = setup_initial_state()
    execute_commands(blp, TEST_CASES[number])
    blp.display_state()


def main():
    parser = argparse.ArgumentParser(description="BLP case screenshot walkthrough")
    parser.add_argument("--case", type=int, choices=range(1, 19), metavar="1-18", help="Show just one numbered case")
    args = parser.parse_args()
    cases = [args.case] if args.case is not None else range(1, 19)
    print("Lab 5 manual screenshot walkthrough")
    print("Expand the Terminal window so the case output is visible.")
    print("Take a full-screen screenshot, then annotate the CASE block with a red rectangle.")
    for number in cases:
        show_case(number)
        input(f"[Screenshot Case {number} now; press Enter to continue] ")
    print("All selected cases finished.")


if __name__ == "__main__":
    main()
