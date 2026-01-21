import pytest
from fairsharer import fair_sharer

def test_fair_sharer_scenario_1():
    """Testet Beispiel 1 aus der PDF: 1 Iteration"""
    values = [0, 1000, 800, 0]
    result = fair_sharer(values, 1)
    # 1000 ist max. Gibt 100 an 0 (links) und 800 (rechts).
    # 0 -> 100
    # 1000 -> 800
    # 800 -> 900
    # 0 -> 0
    assert result == [100, 800, 900, 0]

def test_fair_sharer_scenario_2():
    """Testet Beispiel 2 aus der PDF: 2 Iterationen"""
    values = [0, 1000, 800, 0]
    result = fair_sharer(values, 2)
    # Nach Iteration 1: [100, 800, 900, 0]
    # Max ist 900. Share ist 90.
    # 900 gibt an 800 (links) und 0 (rechts).
    # 800 + 90 = 890
    # 0 + 90 = 90
    # 900 - 180 = 720
    assert result == [100, 890, 720, 90]