def calculate(data, findall):
    matches = findall(r'([abc])([+-]?[=])([abc]?)([+-]?\d+)?')  # Если придумать хорошую регулярку, будет просто
    for v1, s, v2, n in matches:  # Если кортеж такой структуры: var1, [sign]=, [var2], [[+-]number]
        right_part = data.get(v2, 0) + int(n or 0)
        if s[0] == '+':
            data[v1] += right_part
        elif s[0] == '-':
            data[v1] -= right_part
        else:
            data[v1] = right_part

    return data
