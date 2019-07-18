#!/usr/bin/env python
#
#This file is part of "jiffy".
#
#Project: jiffy: A product for building and managing infrastructure: 
#cloud provider services, and servers and their configurations.
#
#Description: A product for building and managing infrastructure. 
#This includes third party API calls for services such as virtual
#cloud servers, load balancers, databases, and other. The product 
#manages connectivity and appropriate communication among these 
#resources.
#
#Copyright (C) Gary Leong - All Rights Reserved
#Unauthorized copying of this file, via any medium is strictly prohibited
#Proprietary and confidential
#Written by Gary Leong  <gwleong@gmail.com>, March 17,2017

# content of test_sample.py
def func(x):
    return x + 1

def test_answer():
    assert func(5) == 5
    #assert func(4) == 5
