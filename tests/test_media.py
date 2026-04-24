import pytest
from src.operazioni import media

def test_media():
    assert media([5,6,7,3,9])==6

def test_media_vuota():
    assert media([])=="lista vuota"

