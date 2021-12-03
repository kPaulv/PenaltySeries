class FootballTeams:
    Pa = 0.65
    Pb = 0.45
    Sa = 0
    Sb = 0
    N = 0

    def __init__(self, tpa, tpb, tsa, tsb, tn):
        self.N = tn
        self.Pa = tpa
        self.Pb = tpb
        self.Sa = tsa
        self.Sb = tsb

    def set_score(self, tsa, tsb):
        self.Sa = tsa
        self.Sb = tsb

    def set_n(self, tn):
        self.N = tn

    def set_prob(self, tpa, tpb):
        self.Pa = tpa
        self.Pb = tpb


# probability of n successes
def prob_equals(n, p):
    return pow(p, n)


# probability of n successes
def prob_success(n, p, s, nn):
    return pow(p, n)


# probability of unsuccessful penalty
def prob_no_success(n, p):
    count = n
    pr = 1
    while count > 0:
        pr *= (1 - p)
        count -= 1
    return pr


# probability of less than n successes
def prob_less(n, p, s, nn):
    sp = 0
    # for i in range(n - 1):
    # sp += pow(p, i)
    count = n
    t = 1
    sp += pow(1 - p, n)
    while count - t > 0:
        sp += prob_equals(count - t, p) * prob_no_success(t, p)
        t += 1

    # sp = prob_equals(n - 1, p) * prob_no_success(1, p) +

    return sp


def success(n, p):
    return pow(p, n)


def less(n, p):
    s = pow(1 - p, n)
    c = n - 1
    while c > 0:
        s += pow(p, c) * pow(1 - p, n - c)
        c -= 1
    return s


# probability of team A winning 5 penalty series
def prob_win_a(pa, pb, sa, sb, n):
    first_series = 5
    nn = n
    p = 0
    while first_series - sa > 0 or first_series - sb > 0:
        # p += prob_success(first_series, pa, sa, n) * prob_less(first_series, pb, sb, n)
        p += success(first_series, pa) * less(first_series, pb)
        first_series -= 1
        nn += 1

    p = (pow(0.65, 5) * (pow(0.55, 5) + 0.45 * pow(0.55, 4) + pow(0.45, 2) * pow(0.55, 3) + pow(0.45, 3) * pow(0.55, 2) +
                     pow(0.45, 4) * pow(0.55, 1))) + (pow(0.65, 4) * (pow(0.55, 5) + 0.45 * pow(0.55, 4) + pow(0.45, 2)
                                                                      * pow(0.55, 3) + pow(0.45, 3) * pow(0.55, 2))) + \
    (pow(0.65, 3) * (pow(0.55, 5) + 0.45 * pow(0.55, 4) + pow(0.45, 2) * pow(0.55, 3))) + \
    (pow(0.65, 2) * (pow(0.55, 5) + 0.45 * pow(0.55, 4))) + (0.65 * (pow(0.55, 5)))
    '''
    p = prob_success(5, pa) * prob_less(5, pb) + prob_success(4, pa) * prob_less(4, pb) + \
        prob_success(3, pa) * prob_less(3, pb) + prob_success(2, pa) * prob_less(2, pb) + \
        prob_success(1, pa) * prob_no_success(5, pb)
    '''
    print(p)


Pa = 0.65
Pb = 0.45
Sa = 0
Sb = 0
N = 0
prob_win_a(Pa, Pb, Sa, Sb, N)
