#!/usr/bin/env python
#
# content of test_sample.py
#

def func(x):
    return x + 1

def test_answer():
    #assert func(5) == 5
    assert func(4) == 5

test_answer()
