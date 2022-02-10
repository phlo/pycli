import pycli
import sys
import unittest

app = "main"

def run (argv=[]):
    sys.argv = [app] + argv
    return pycli.run()

class Main (unittest.TestCase):

    #
    # utility functions
    #

    def expect_success (self, module):
        args = ["pos0", "-opt0", "opt0"]
        try:
            ret = run(module + args)
            self.assertEqual(ret["argv"], [" ".join([app] + module)] + args)
            self.assertEqual(ret["args"].pos0, "pos0")
            self.assertEqual(ret["args"].opt0, "opt0")
        except SystemExit as e:
            self.fail()

    def expect_failure (self, args=[]):
        with self.assertRaises(SystemExit) as e:
            run(args)
        self.assertNotEqual(e.exception.code, 0)

    #
    # test functions
    #

    def test_call_no_args (self):
        self.expect_failure()

    # m0

    def test_call_m0_no_args (self):
        self.expect_failure(["m0"])

    def test_call_m0_with_args (self):
        self.expect_success(["m0"])

    def test_call_m0_with_illegal_args (self):
        self.expect_failure(["m0", "foo", "bar"])

    # p0

    def test_call_p0 (self):
        self.expect_failure(["p0"])

    # p0 m0

    def test_call_p0_m0_no_args (self):
        self.expect_failure(["p0", "m0"])

    def test_call_p0_m0_with_args (self):
        self.expect_success(["p0", "m0"])

    def test_call_p0_m0_with_illegal_args (self):
        self.expect_failure(["p0", "m0", "foo", "bar"])

    # p0 p00

    def test_call_p0_p00 (self):
        self.expect_failure(["p0", "p00"])

    #  # p0 p00 m00

    def test_call_p0_p00_m00_no_args (self):
        self.expect_failure(["p0", "p00", "m00"])

    def test_call_p0_p00_m00_with_args (self):
        self.expect_success(["p0", "p00", "m00"])

    def test_call_p0_p00_m00_with_illegal_args (self):
        self.expect_failure(["p0", "p00", "m00", "foo", "bar"])
