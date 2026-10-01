import pytest
import utils

def test_get_int(monkeypatch):
    monkeypatch.setattr("builtins.input",lambda message:"2")
    result = utils.get_int(1,3,"")
    assert result == 2
    inputs = iter(["4","2"])
    monkeypatch.setattr("builtins.input",lambda _: next(inputs))
    result = utils.get_int(1,3,"")
    assert result == 2

def test_yes_no(monkeypatch):
    monkeypatch.setattr("builtins.input",lambda message: "y")
    assert utils.yes_no("") == 'y'

#utils.get_int()