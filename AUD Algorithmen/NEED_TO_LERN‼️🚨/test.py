def fib_memoized(n, cache={}):

    if n <= 1:
        return n
    elif n in cache:
        return cache[n]
    cache[n] = fib_memoized(n - 1, cache) + fib_memoized(n - 2, cache)  # ✅ Wert speichern!
    return cache[n]

def fib_bottomup(n):
    t = []
    t.append(0)
    t.append(1)
    for i in range(2, n+1):
        t.append(t[i-1] + t[i-2])

    return t[n]

def expontent(n):
    result = 1
    for i in range(1, n+1):
        result *= 2
    return result
def exponent_bottom_up(n):
    t =[]
    t.append(1)
    for i in range(1, n+1):
        t.append(t[i-1]*2)
    return t[n]
def exponent_top_down(n,memo={}):
    if n == 0:
        return 1
    elif n in memo:
        return memo[n]
    memo[n] = exponent_top_down(n-1,memo)*2
    return memo[n]

def multiplikation(a,b):
    def teilen(a,b):
        c=a
        r = 0
        while b <=c:
            c = c-b
            r += 1
        return r
    if b== 0:
        return 0
    if b == 1:
        return a
    h = teilen(b,2)
    return multiplikation(a,h)+multiplikation(a,b-h)

def bottomup_multiplier(a,b):
    t = []
    t.append(0)
    t.append(a)
    for i in range(2, b+1):
        t.append(t[i-1]+a)
    print(t)
    return t[b]



def topdown_multiplier(a,b, memo={}):
    if b == 0:
        return 0
    if b==1:
        return a
    if b in memo:
        return memo[b]
    memo[b] = topdown_multiplier(a,b-1,memo)+a
    return memo[b]



def power_bbtm(base,exponent):
    t = []
    t.append(0)
    t.append(base)
    for i in range(2,exponent+1):
        t.append(t[i-1]*base)
    return t[exponent]

def power_memo(base,exponent,memo={}):

    if exponent ==0:
        return 1
    if exponent==1:
        return base
    if exponent in memo:
        return memo[exponent]
    memo[exponent] = power_memo(base,exponent-1,memo)*base
    return memo[exponent]



print(power_bbtm(5,3))
print(power_memo(5,3,memo={}))