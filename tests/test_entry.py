import pytest
import entry

def test_select_category(monkeypatch):
    monkeypatch.setattr("builtins.input",lambda message:"2")
    result = entry.select_category(["category1","category2","category3","category4"])
    assert result == "category2"