n = int(input())

if n > 20:
    print(2**n - 1)
else:
    plate = n
    s = 1
    m = 2
    e = 3
    move = []

    def hanoi(plate, s, m, e):
        if plate == 0:
            return
        hanoi(plate - 1, s, e, m)
        move.append(f"{s} {e}")
        hanoi(plate - 1, m, s, e)

    hanoi(plate, s, m, e)
    
    print(len(move))
    for m in move:
        print(m)