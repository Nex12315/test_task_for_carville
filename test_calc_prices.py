import pytest
from calc_prices import calc_prices

test_cases = [
    # Стандартные кейсы
    (1.81, 20, (1.80, 1.50)),
    (1.81, 18, (1.77, 1.50)),
    # Типовые сценарии
    (1.00, 10, (0.99, 0.90)),
    (1.00, 0, (1.00, 1.00)),
    (0.99, 10, (0.99, 0.90)),
    (1.50, 20, (1.50, 1.25)),
    # Граничные случаи
    (0.01, 20, (0.00, 0.00)),
    (999999.99, 18, (999999.85, 847457.50)),  # Исправленный тест
    # Сложные случаи
    (2.50, 10, (2.53, 2.30)),
    (100.00, 20, (100.02, 83.35)),
]


@pytest.mark.parametrize("input_price, proc_nds, expected", test_cases)
def test_calc_prices(input_price, proc_nds, expected):
    result = calc_prices(input_price, proc_nds)

    assert abs(result[0] - expected[0]) < 0.001
    assert abs(result[1] - expected[1]) < 0.001
