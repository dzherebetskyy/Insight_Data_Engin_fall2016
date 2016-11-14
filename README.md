Written by Danylo Zherebetskyy in Python on November 13,2016 for Insight Data Engineering - Coding Challenge

The problem solution code: antifraud.py uploaded at 9pm

There was a problem: the run_tests.sh in insight_testsuite/ removed my code from the src directory and all the generated data-files (output1.txt, output2.txt, output3.txt), so in the result it did not pass the grader (at 9pm). Need to fix this problem.

Fixing the problem (11pm): required to look in the BASH-script, figured out that the BASH-script copies the src-content from the main src-directory into the insight_testsuite/ and then runs the code. So, I just had to copy the code in the main src-directory; passed the grader (Python-code remain unchanged since 9pmn).

New zip-master with passed predesigned tests and own created tests: digital-wallet-master_DZ.zip [Sun Nov 13]
[PASS]: test-1-paymo-trans (output1.txt)
[PASS]: test-1-paymo-trans (output2.txt)
[PASS]: test-1-paymo-trans (output3.txt)
[PASS]: test_my (output1.txt)
[PASS]: test_my (output2.txt)
[PASS]: test_my (output3.txt)
[PASS]: your-own-test (output1.txt)
[PASS]: your-own-test (output2.txt)
[PASS]: your-own-test (output3.txt)


The python-code requires to: import sys

Cons: Works with data up to several-GB

