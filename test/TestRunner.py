from unittest import TestLoader, TestSuite, TextTestRunner
from admintest import admintest
from staffTest import staffTest
from residentTest import residentTest
from ResetPassword import ResetPassword
from signupFeature import signupFeature

if __name__ == "__main__":
    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(signupFeature),
        loader.loadTestsFromTestCase(ResetPassword),
        loader.loadTestsFromTestCase(residentTest),
        loader.loadTestsFromTestCase(staffTest),
        loader.loadTestsFromTestCase(admintest),

    ))

    runner = TextTestRunner(verbosity=2)
    runner.run(suite)
