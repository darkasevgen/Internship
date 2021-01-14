import numpy as np

# вероятность просмотра фильма на k-ый день после сбора статистики (прошлого вечера)
prob_elki, prob_ironia, prob_odin = np.array(0, dtype=np.float64), np.array(0, dtype=np.float64), np.array(0, dtype=np.float64)

# вероятность просмотра фильма за k-а дней (не учитывая прошлый вечер)
prob_all_elki, prob_all_ironia, prob_all_odin = np.array(0, dtype=np.float64), np.array(0, dtype=np.float64), np.array(0, dtype=np.float64)


def ironia(prob, k):
    global prob_ironia, prob_all_ironia
    if k == 0:
        prob_ironia += prob
        return prob
    else:
        prob_all_ironia += prob
        odin_doma(prob * 0.3, k - 1)
        ironia(prob * 0.7, k - 1)

def odin_doma(prob, k):
    global prob_odin, prob_all_odin
    if k == 0:
        prob_odin += prob
        return prob
    else:
        prob_all_odin += prob
        elki(prob * 0.5, k - 1)
        ironia(prob * 0.5, k - 1)

def elki(prob, k):
    global prob_elki, prob_all_elki
    if k == 0:
        prob_elki += prob
        return prob
    else:
        prob_all_elki += prob
        odin_doma(prob * 0.2, k - 1)
        ironia(prob * 0.8, k - 1)

k = 8
# начальная вероятность = 1, т.к. в прошлый вечер точно просмотрен фильм 'Ёлки'
elki(prob=np.array(1., dtype=np.float64), k=k)
print(f'k = {k}')
print(f"Вероятность просмотра фильма 'Ёлки' в k-ый вечер = {prob_elki}, \n'Ирония судьбы' = {prob_ironia}, \n'Один дома' = {prob_odin}")

print(f"Ожидаемое количество просмотров фильма 'Ёлки' за k-а вечеров = {prob_all_elki}, \n'Иронии судьбы' = {prob_all_ironia}, \nфильма 'Один дома' = {prob_all_odin}")

# == k (т.к. за k вечеров будет просмотрено k фильмов)
print(f"Сумма = {prob_all_elki + prob_all_ironia + prob_all_odin}")

print(f"Доля показов 'Ёлки' за k-а вечеров = {prob_all_elki / k}, \n'Иронии судьбы' = {prob_all_ironia / k}, \nфильма 'Один дома' = {prob_all_odin / k}")