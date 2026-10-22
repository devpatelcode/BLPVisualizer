"""Independent assertions for all 18 assignment test scenarios."""
from contextlib import redirect_stdout
from io import StringIO
from Cases import TEST_CASES, setup_initial_state

EXPECTED_ACTIONS = {
    1: [True], 2: [False], 3: [True], 4: [False], 5: [False],
    6: [True, False], 7: [True, True],
    8: [True, True, True, False],
    9: [True, False, False, True],
    10: [True, True, True], 11: [True, True, False],
    12: [True, True, False], 13: [True, True, False],
    14: [True, False, True], 15: [True, True],
    16: [True, False, False, True],
    17: [True, False, False, False],
    18: [True, False],
}


def check():
    for case_number, commands in sorted(TEST_CASES.items()):
        stream = StringIO()
        with redirect_stdout(stream):
            blp = setup_initial_state()
            actual = []
            for action, *args in commands:
                actual.append(getattr(blp, action)(*args))
        assert actual == EXPECTED_ACTIONS[case_number], (
            f"Case {case_number} returned {actual}, expected {EXPECTED_ACTIONS[case_number]}"
        )
        print(f"Case {case_number:2}: PASS | steps: {', '.join('ALLOW' if v else 'DENY' for v in actual)}")
    print("Verified: all 18 cases and 44 action results passed.")


if __name__ == "__main__":
    check()
