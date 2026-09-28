import pytest
import utils

def test_get_int(monkeypatch):
    monkeypatch.setattr("builtins.input",lambda message:"2")
    result = utils.get_int(1,3,"")
    assert result == 2

#utils.get_int()