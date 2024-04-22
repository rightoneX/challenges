def pageCount(n, p):
    ld = n - p
    fd = p - 1
    if (ld) <= (fd):
        if n % 2 != 0:
            return ld // 2
        else:
            if ld % 2 != 0:
                return (ld + 1) // 2
        return ld // 2
    else:
        if fd % 2 != 0:
            return (fd + 1) // 2
    return fd // 2



print(pageCount(6, 2))