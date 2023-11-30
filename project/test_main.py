import unittest
import glob


def run_tests():
    suite = unittest.TestLoader().discover("tests", pattern="test*.py")
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    return result.wasSuccessful()


if __name__ == "__main__":
    # BEGIN: ed8c6549bwf9
    test_files = glob.glob("tests/test*.py")
    if run_tests():
        print("All tests passed!")
    else:
        print("Some tests failed.")
    # END: ed8c6549bwf9
