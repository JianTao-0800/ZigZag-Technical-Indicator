def zigzag(s, c=0.05):
    """ 
    The Zig Zag indicator plots points on the chart whenever prices reverse by or greater than
    a pre-chosen variable. Straight lines are then drawn, connecting these points. The indicator
    is used to help identify price trends. It eliminates random price fluctuations and attempts
    to show trend changes. Zig Zag lines only appear when there is a price movement between a
    swing high and a swing low that is greater than a specified variable.

    >>> s1 = [0, 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6]
    >>> zigzag(s1, c=5)
    [7, 0]
    >>> s2 = [0, 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6,
    ...       5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4]
    >>> zigzag(s2, c=5)
    [7, 0, 6, 1, 9]
    """    
    zz = []
    signal = 0
    inflection = s[0]
    
    for i in range(1, len(s)):
        # Find first trend
        if signal == 0:
            if s[i] <= (inflection - c):
                signal = -1
            if s[i] >= (inflection + c):
                signal = 1

        # Downtrend, inflection keeps track of the lowest point in the downtrend
        if signal == -1:
            # New Minimum, change inflection
            if s[i] < inflection:
                inflection = s[i]
            # Trend Reversal
            if s[i] >= (inflection + c):
                signal = 1
                zz.append(inflection)  # Append the lowest point of the downtrend to zz
                inflection = s[i]      # Current point becomes the highest point of the new uptrend
                continue

        # Uptrend, inflection keeps track of the highest point in the uptrend
        if signal == 1:
            # New Maximum, change inflection
            if s[i] > inflection:
                inflection = s[i]
            # Trend Reversal
            if s[i] <= (inflection - c):
                signal = -1
                zz.append(inflection)  # Append the highest point of the uptrend to zz
                inflection = s[i]      # Current point becomes the lowest point of the new trend
                continue
    return zz


if __name__ == "__main__":
    import doctest
    doctest.testmod()
