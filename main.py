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
def prob_success(n, p):
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
def prob_less(n, p):
    sp = 0
    # for i in range(n - 1):
    # sp += pow(p, i)
    count = n
    t = 1
    while count - t > 0:
        sp += prob_equals(count - t, p) * prob_no_success(t, p)
        t += 1

    # sp = prob_equals(n - 1, p) * prob_no_success(1, p) +

    return sp


# probability of team A winning 5 penalty series
def prob_win_a(pa, sa, pb, sb, n):
    p = prob_success(5, pa) * prob_less(5, pb) + prob_success(4, pa) * prob_less(4, pb) + \
        prob_success(3, pa) * prob_less(3, pb) + prob_success(2, pa) * prob_less(2, pb) + \
        prob_success(1, pa) * prob_no_success(5, pb)
    print(p)
