from fairsharer import fair_sharer

def test_fair_sharer_scenario_1():
    """Testet Beispiel 1 aus der PDF: 1 Iteration"""
    values = [0, 1000, 800, 0]
    result = fair_sharer(values, 1)
    assert result == [100, 800, 900, 0]

def test_fair_sharer_scenario_2():
    """Testet Beispiel 2 aus der PDF: 2 Iterationen"""
    values = [0, 1000, 800, 0]
    result = fair_sharer(values, 2)
    assert result == [100, 890, 720, 90]