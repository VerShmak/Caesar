# Лабораторная работа №1 "Шифр Цезаря"
В ходе даной работы требуется реализовать:  
 - Шифрование текста
 - Дешифрование текста
 - Фукцию взлома шифра

# Описание алгоритма шифрования
Шифр Цезаря — это простой алгоритм симметричного шифрования, который использует метод сдвига букв в алфавите.

В качестве ключа используется целое число, указывающее на сколько позиций нужно сдвинуть каждую букву.
После ввода текста, который требуется зашифровать, выберите величину шага. 

Для каждой буквы в исходном тексте определяется её позиция в алфавите. Даная позиция сдвигается на значение ключа. Если сдвиг выходит за пределы алфавита, то происходит возвращение к началу алфавита (например, после 'Я' снова 'А'). В конечном итоге происходит замена буквы на новую, полученую после сдвига.

# Описание алгоритма дешифрования
Для расшифровки текста выполняется сдвиг в обратном направлении (вычтается значение ключа).

# Описание алгоритма взлома
Чтобы взломать зашифрованный текст, программа анализирует частоту появления букв и выбирает самый вероятный вариант сдвига. 

# Тестовое задание 
Исходный текст:

To make a pumpkin pie, mix one cup of pumpkin puree, three fourths cup of sugar, one teaspoon of cinnamon, half a teaspoon of nutmeg, half a teaspoon of salt, two eggs, and one can of evaporated milk, pour into a pie crust, and bake at four hundred degrees Fahrenheit for forty five minutes.

Выбранный шаг: 5

#  Результат шифрования
Yt rfpj f uzrupns unj, rnc tsj hzu tk uzrupns uzwjj, ymwjj ktzwymx hzu tk xzlfw, tsj yjfxutts tk hnssfrts, mfqk f yjfxutts tk szyrjl, mfqk f yjfxutts tk xfqy, ybt jllx, fsi tsj hfs tk jafutwfyji rnqp, utzw nsyt f unj hwzxy, fsi gfpj fy ktzw mzsiwji ijlwjjx Kfmwjsmjny ktw ktwyd knaj rnszyjx.

# Результат дешифрования
To make a pumpkin pie, mix one cup of pumpkin puree, three fourths cup of sugar, one teaspoon of cinnamon, half a teaspoon of nutmeg, half a teaspoon of salt, two eggs, and one can of evaporated milk, pour into a pie crust, and bake at four hundred degrees Fahrenheit for forty five minutes.

# Результат взлома
Текст для  взлома: 
Fa ymwq m bgybwuz buq, yuj azq ogb ar bgybwuz bgdqq, ftdqq ragdfte ogb ar egsmd, azq fqmebaaz ar ouzzmyaz, tmxr m fqmebaaz ar zgfyqs, tmxr m fqmebaaz ar emxf, fia qsse, mzp azq omz ar qhmbadmfqp yuxw, bagd uzfa m buq odgef, mzp nmwq mf ragd tgzpdqp pqsdqqe Rmtdqztquf rad radfk ruhq yuzgfqe.

Результат при 12 шаге:
To make a pumpkin pie, mix one cup of pumpkin puree, three fourths cup of sugar, one teaspoon of cinnamon, half a teaspoon of nutmeg, half a teaspoon of salt, two eggs, and one can of evaporated milk, pour into a pie crust, and bake at four hundred degrees Fahrenheit for forty five minutes.


