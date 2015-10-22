A,B,C,D,E,F,G,H = 0,0,1,1,-1,-1,2,2


def area(a,b,c,d):
    return (c - a) * (d - b)

def add(A,B,C,D,E,F,G,H):
    if A <= E:
        if B >= H:
            return area(A,B,C,D)

        elif F < B < H:
            if C <= E:
                return area(A,B,C,D)
            elif E < C < G:
                if D > H:
                    return area(A,B,C,D) + area(E,F,G,H) - area(E,B,C,H)
                else:
                    return area(A,B,C,D) + area(E,F,G,H) - area(E,B,C,D)
            else:
                if D > H:
                    return area(A,B,C,D) + area(E,F,G,H) - area(E,B,G,H)
                else:
                    return area(A,B,C,D) + area(E,F,G,H) - area(E,B,G,H)
        else:
            if C <= E:
                return area(A,B,C,D)
            elif E < C < G:
                if D <= F:
                    return area(A,B,C,D)
                elif F < D < H:
                    return area(A,B,C,D) + area(E,F,G,H) - area(E,F,C,D)
                else:
                    return area(A,B,C,D) + area(E,F,G,H) - area(E,F,G,D)
            else:
                if D <= F:
                    return area(A,B,C,D)
                elif F < D < H:
                    return area(A,B,C,D) + area(E,F,G,H) - area(E,F,G,D)
                else:
                    return area(A,B,C,D) 
    elif E < A < G:
        if B <= F:
            if C <= G:
                if D <= F:
                    return area(A,B,C,D) 
                elif F < D < H:
                    return area(A,B,C,D) + area(E,F,G,H) - area(A,F,C,D)
                else:
                    return area(A,B,C,D) + area(E,F,G,H) - area(A,F,C,H)
            else:
                if D <= F:
                    return area(A,B,C,D) 
                elif F < D < H:
                    return area(A,B,C,D) + area(E,F,G,H) - area(A,F,G,D)
                else:
                    return area(A,B,C,D)
        elif F < B < H:
            if C < G:
                if D < H:
                    return area(E,F,G,H)
                else:
                    return area(A,B,C,D) + area(E,F,G,H) - area(A,B,C,H)
            else:
                if D < H:
                    return area(A,B,C,D) + area(E,F,G,H) - area(A,B,G,D)
                else:
                    return area(A,B,C,D) + area(E,F,G,H) - area(A,F,G,H)
        else:
            return area(A,B,C,D)

    else:
        return area(A,B,C,D)

print add(A,B,C,D,E,F,G,H )













            









