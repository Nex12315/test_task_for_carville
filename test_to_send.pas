unit Unit1;

interface

type
  TProcNDS = 0..99;

procedure CalcPrices(InputPriceWithNDS: double; ProcNDS: TProcNDS; out CorrectedPriceWithNDS, CorrectedPriceWithoutNDS: double);

implementation

procedure CalcPrices(InputPriceWithNDS: double; ProcNDS: TProcNDS; out CorrectedPriceWithNDS, CorrectedPriceWithoutNDS: double);
begin
//  Есть правило:
//  [Цена с НДС] = [Цена без НДС] * (1 + [Процент НДС] / 100)
//  Или запишем иначе
//  CorrectedPriceWithNDS = CorrectedPriceWithoutNDS * (1 + ProcNDS / 100)

//  Входные параметры процедуры:
//  1. Внешняя система рассчитывает и передает нам рекомендованную цену с НДС - InputPriceWithNDS,
//  содержащую до 20 знаков после зарпятой
//  2. Процент НДС  -  ProcNDS : 0..99

//  ЗАДАЧА: Процедура должна рассчитать значение цен с НДС и без НДС (CorrectedPriceWithNDS,
//  CorrectedPriceWithoutNDS) так, чтобы CorrectedPriceWithNDS была предельно близко
//  к InputPriceWithNDS: |CorrectedPriceWithNDS-InputPriceWithNDS| -> min ...  и при этом
//  CorrectedPriceWithNDS и CorrectedPriceWithoutNDS содержали максимум 2 знака после
//  запятой и не требовали округлений.

//  Например -
//  CalcPrices(1.81, 20, CorrectedPriceWithNDS, CorrectedPriceWithoutNDS)
//  должна вернуть -
//  CorrectedPriceWithNDS     = 1.8
//  CorrectedPriceWithoutNDS  = 1.5
//
//  CalcPrices(1.81, 18, CorrectedPriceWithNDS, CorrectedPriceWithoutNDS)
//  должна вернуть -
//  CorrectedPriceWithNDS     = 1.77
//  CorrectedPriceWithoutNDS  = 1.5
//	Подумайте над другими вариантами проверки корректности вашего алгоритма.
//  3. Сделать интерфейс для проверки корректности вашего решения. Используем только стандартные библиотеки.
//  4. Прислать в архиве на почту все файлы проекта. В случае проблем с отправкой установить пароль 123.
end;

end.
