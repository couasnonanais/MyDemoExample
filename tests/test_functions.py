# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 13:52:00 2018

@author: Anton
"""

from functions import *
import mock
from mock import patch , Mock

#Test functions have to start with test

def test_awesome_function():
    expected_value = 42
    actual_value = awesome_function()
    assert expected_value == actual_value, 'Value doesnot match'
    
def test_something_else():
    assert 1 == 1 , 'doesnot work'
   
@patch('requests.get')
def test_text_analysis(mock_call):
    mock_call.return_value = Mock()
    mock_call.return_value.text = 'fake text'
    wc = do_text_analysis()
    assert wc > 0, 'Text should have more than 0 length'