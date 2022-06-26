def oddTuples(aTup):
    """
    aTup: a tuple

    returns: tuple, every other element of aTup.
    """
    odd = 0
    oddTup = ()
    for tup in aTup:
        odd += 1
        if odd % 2 != 0:
            oddTup = oddTup + (tup,)
        else:
            continue
    return oddTup


print(oddTuples(("I", "am", "a", "test", "tuple")))
print(type(oddTuples(("i", "am", "a", "typle"))))
