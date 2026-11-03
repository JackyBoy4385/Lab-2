
import Lab2

def test_find_min_max():
    num_list = [10, 20, 30, 40, 50]
    result = Lab2.find_min_max(num_list)
    assert result == [10, 50]


def test_calc_average():
    num_list = [10, 20, 30, 40, 50]
    result = Lab2.calc_average(num_list)
    assert result == 30


def test_calc_median_temperature_odd():
    num_list = [10, 20, 30, 40, 50]
    result = Lab2.calc_median_temperature(num_list)
    assert result == 30


def test_calc_median_temperature_even():
    num_list = [10, 20, 30, 40]
    result = Lab2.calc_median_temperature(num_list)
    assert result == 25
