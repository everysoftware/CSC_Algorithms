from collections import deque


def net_packets(size, n, arrival, duration):
    # Задание параметра maxlen позволяет не заботиться об удалении элементов из очереди:
    # при добавлении элемента в заполненную очередь первый элемент в очереди будет удален
    q = deque([0] * size, maxlen=size)
    result = []
    for i in range(n):
        # новый пакет реально обработать только если он пришёл
        # либо после первого пакета в очереди, либо в тот же самый момент
        if arrival[i] >= q[0]:
            # текущий пакет начнёт обрабатываться либо непосредственно
            # в момент его прибытия arrival[i],
            # либо в момент окончания обработки последнего пакета
            result.append(max(q[-1], arrival[i]))
            # добавляем в очередь момент окончания обработки текущего пакета
            q.append(max(q[-1], arrival[i]) + duration[i])
        else:
            result.append(-1)
    return result
