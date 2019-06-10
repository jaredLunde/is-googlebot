#!/usr/bin/python3 -S
# -*- coding: utf-8 -*-
import os
import sys


cd = os.path.dirname(os.path.abspath(__file__))
path = cd.split('is_googlebot')[0] + 'is_googlebot'
sys.path.insert(0, path)


def main():
    import pytest
    pytest.main([os.path.dirname(os.path.realpath(__file__))])
