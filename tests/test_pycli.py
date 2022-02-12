import sys
import unittest

from . import run

class Run (unittest.TestCase):

    #
    # utility functions
    #

    def expect_success (self, module: list[str]):
        args = ["pos0", "-opt0", "opt0"]
        try:
            ret = run(module + args)
            self.assertEqual(ret["argv"][1:], args)
            self.assertEqual(ret["args"].pos0, "pos0")
            self.assertEqual(ret["args"].opt0, "opt0")
        except SystemExit as e:
            self.fail()

    def expect_failure (self, module: list[str] = []):
        with self.assertRaises(SystemExit) as e:
            run(module)
        self.assertNotEqual(e.exception.code, 0)

    #
    # test functions
    #

    def test_run_no_args (self):
        self.expect_failure()

    # m0

    def test_run_m0_no_args (self):
        self.expect_failure(["m0"])

    def test_run_m0_with_args (self):
        self.expect_success(["m0"])

    def test_run_m0_with_illegal_args (self):
        self.expect_failure(["m0", "foo", "bar"])

    # p0

    def test_run_p0 (self):
        self.expect_failure(["p0"])

    # p0 m0

    def test_run_p0_m0_no_args (self):
        self.expect_failure(["p0", "m0"])

    def test_run_p0_m0_with_args (self):
        self.expect_success(["p0", "m0"])

    def test_run_p0_m0_with_illegal_args (self):
        self.expect_failure(["p0", "m0", "foo", "bar"])

    # p0 p00

    def test_run_p0_p00 (self):
        self.expect_failure(["p0", "p00"])

    #  # p0 p00 m00

    def test_run_p0_p00_m00_no_args (self):
        self.expect_failure(["p0", "p00", "m00"])

    def test_run_p0_p00_m00_with_args (self):
        self.expect_success(["p0", "p00", "m00"])

    def test_run_p0_p00_m00_with_illegal_args (self):
        self.expect_failure(["p0", "p00", "m00", "foo", "bar"])
