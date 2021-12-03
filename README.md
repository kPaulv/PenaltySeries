# PenaltySeries

Тестовое задание
В основе решения лежит схема Бернулли. Для нахождения вероятности победы команды А в серии пенальти необходимо находить вероятность успеха для некоторого количетва ударов.
Рассмотрим серию из 5 ударов, счёт 0:0, вероятности гола - Pa и Pb. введём переменные для числа успешно сделанных ударов - na и nb. 
Тогда вероятность победы команды а в серии из 5 ударов складывается из вероятностей событий типа "успешных исходов у команды А больше, чем у команды B": 
P = P(na = 5)*P(nb < 5) + ... P(na = 1)*P(nb=0). 
Далее следует рассмотреть ситуацию, при которой в серии из 5 ударов результат ничейный. Вероятность назначения дополнительной серии пенальти складывается из вероятностей событий 
типа "успехов А столько же, сколько и B":
Pd = P(na = 5)*P(nb = 5) + P(na = 4)*P(nb = 4) + P(na = 3)*P(nb = 3) + P(na = 2)*P(nb = 2) + P(na = 1)*P(nb = 1) + P(na = 0)*P(nb = 0)
Далее рассмотрим вероятность выигрыша в доп. серии. Правила для доп серии таковы, что победа присуждается как только при равном количестве ударов у одной команды будет больше очков.
Вероятность победы команды А для 1 удара - P1' = Pa*(1 - Pb), (1 - Pb) - вероятность неуспеха команды B. Однако может быть сделан не 1 удар, прежде чем будет определён победитель.
Для команды B дополнительной серии - P2' = Pb*(1 - Pa). Найдём вероятность P1 - победа команды А во всей доп. серии. для любого количества ударов отношение P1 к P2 будет неизменно 
и равно P1/P2 = P1'/P2' = Pa*(1-Pb)/(Pb*(1-Pa)). Из соотношения выразим P1 = Pa*(1-Pb)/(Pa*(1-Pb) + Pb*(1-Pa))
Итоговая вероятность победы команды А будет равна:
P0 = P + Pd*P1. Т.е. сумма вероятности события "победа А в осн. серии" + вероятности события "введение доп. серии и победа в ней команды А"
В нетривиальном случае при уже имеющемся счёте и пробитых ударах, их следует учесть в формуле нахождения вероятности n-го количества успехов.