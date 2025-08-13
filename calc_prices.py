import math
from decimal import Decimal, ROUND_FLOOR, ROUND_HALF_UP


def calc_prices(input_price_with_nds, proc_nds):
    # Конвертация входной цены в Decimal для точных вычислений
    input_price_decimal = Decimal(str(input_price_with_nds))

    # Вычисление множителя НДС (100 + процент НДС)
    nds_multiplier_value = 100 + proc_nds
    if nds_multiplier_value == 0:
        return (0.0, 0.0)

    # Конвертация в Decimal
    nds_multiplier_decimal = Decimal(nds_multiplier_value)

    # Перевод входной цены в копейки
    input_price_in_kopecks = input_price_decimal * Decimal("100")

    # Вычисление НОД для определения шага цены
    gcd_value = math.gcd(100, nds_multiplier_value)

    # Шаг в копейках для цены без НДС
    step_size_kopecks = 100 // gcd_value
    step_size_decimal = Decimal(step_size_kopecks)

    # Рассчет идеальный цены без НДС в копейках
    ideal_price_without_nds_kopecks = (
        input_price_in_kopecks * 100
    ) / nds_multiplier_decimal

    # Нахождение ближайших допустимых значений (кратных шагу)
    step_count = (
        ideal_price_without_nds_kopecks / step_size_decimal
    ).to_integral_value(rounding=ROUND_FLOOR)
    option_low = step_count * step_size_decimal
    option_high = option_low + step_size_decimal

    # Вычисление цены с НДС для каждого варианта
    def calc_with_nds(without_nds_kopecks):
        return (without_nds_kopecks * nds_multiplier_decimal) / Decimal("100")

    option_low_with_nds = calc_with_nds(option_low)
    option_high_with_nds = calc_with_nds(option_high)

    # Выбор варианта с минимальной разницей
    diff_low = abs(option_low_with_nds - input_price_in_kopecks)
    diff_high = abs(option_high_with_nds - input_price_in_kopecks)

    chosen_option = option_low if diff_low <= diff_high else option_high

    # Конвертация обратно в рубли
    price_without_nds_rubles = chosen_option / Decimal("100")
    price_with_nds_rubles = calc_with_nds(chosen_option) / Decimal("100")

    # Округление до двух знаков после запятой
    price_without_nds_rubles = float(
        price_without_nds_rubles.quantize(Decimal("0.00"), rounding=ROUND_HALF_UP)
    )
    price_with_nds_rubles = float(
        price_with_nds_rubles.quantize(Decimal("0.00"), rounding=ROUND_HALF_UP)
    )

    return (price_with_nds_rubles, price_without_nds_rubles)
