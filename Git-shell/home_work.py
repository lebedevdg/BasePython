def funk(test):

    sieve = [True] * test
    for i in range(2, test):
        if sieve[i]:
            print(i)
            for j in range(i*1, test, i):
                sieve[j] = False


funk(10000000)