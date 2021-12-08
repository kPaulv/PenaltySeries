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
    count = n
    t = 1
    sp += pow(1 - p, n)
    while count - t > 0:
        sp += prob_equals(count - t, p) * prob_no_success(t, p)
        t += 1
    return sp


def success(n, total_num, p):
    res = 1
    if n == 0:
        res = pow(1 - p, total_num)
    else:
        res *= pow(p, n) * pow(1 - p, total_num - n)
    return res


def less(n, total_num, p):
    s = 0
    # 0 success
    s += pow(1 - p, total_num)
    for i in range(n - 1):
        s += pow(p, i + 1) * pow(1 - p, total_num - (i + 1))
    return s


# probability of team A winning 5 penalty series
def prob_win_a(pa, pb, sa, sb, n):
    first_series = 5
    nn = 5
    p = 0
    # prob of add. section
    p_section = 0
    # A team wins in 5-penalty section
    while nn > 0:
        p += success(nn, first_series, pa) * less(nn, first_series, pb)
        p_section += success(nn, first_series, pa) * success(nn, first_series, pb)
        nn -= 1
    # A team wins in additional section
    p_win_section = (pa * (1 - pb)) / (pa * (1 - pb) + pb * (1 - pa))
    # Probability of starting additional section and A team winning it
    p_win_section *= p_section
    # A team wins if it wins first section or additional section
    p_total = p + p_win_section

    print(p_total)


print("Enter values. ")
print("Enter probability of successful penalty for team A: ")
Pa = float(input())
print("Enter probability of successful penalty for team B: ")
Pb = float(input())
print("Enter team A score: ")
Sa = float(input())
print("Enter team B score: ")
Sb = float(input())
print("Enter played penalty amount: ")
N = float(input())
# penalty series
total_num = 5
n = 5
prob_win_a(Pa, Pb, Sa, Sb, N)
