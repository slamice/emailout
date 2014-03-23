#!/usr/bin/env python
import pytest
import sys
sys.path.append('..')
import emailer

def test_create_addresses_just_to_address():
    print emailer.create_addresses('me@example.com','you@example.com')
    assert emailer.create_addresses('me@example.com','you@example.com') == ''

def test_check_email_valid_empty_email():
    assert emailer.check_email_valid('') == False

def test_check_email_valid_real_email():
    assert emailer.check_email_valid('user@example.com') == True

def test_add_subject_to_email():
    assert emailer.add_subject_to_email(msg,subject) == 

def test_add_text_to_email():
    assert emailer.add_text_to_email(msg,text) == 
