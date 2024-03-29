# Objective: create the functions to determine probability distributions without any library

def factorial(n):
    """
    Function used to determine factorial of n
    :param n: Integer
    :return: Factorial of n
    """

    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact

def binomial(n, k, p):
    """
    Function used to determine probability using binomial distribution
    :param n: Total number of trials
    :param k: Number of successes
    :param p: The probability of success of 1 trial
    :return: Probability of having exactly k successes out of n trials
    """
    return pow(p, k) * pow(1 - p, n - k) * factorial(n) / (factorial(k) * factorial(n - k))

def geometric(n, p):
    """
    Function used to determine probability using geometric distribution
    :param n: Total number of trials
    :param p: The probability of success of 1 trial
    :return: Probability of having exactly 1 success out of n trials.
    """
    return binomial(n, 1, p)

def poisson(k, lamb):
    """
    Function used to determine probability using poisson distribution
    :param k: Number of successes that occur in a specified region.
    :param lamb: Average number of successes that occur in a specified region
    :return: Probability of getting k exactly  successes when the average number of successes is lambda
    """
    e = 2.71828182845904523536

    return pow(e, -lamb) * pow(lamb, k) / factorial(k)

def normal(x, mu, sigma):
    """
    Function used to determine the probability density of normal distribution
    :param x: Input
    :param mu: Mean of the distribution
    :param sigma: Standard deviation
    :return: Probability density of normal distribution
    """
    e = 2.71828182845904523536
    pi = 3.1415926535897932384

    nominator = e**(- ((x - mu)**2) / (2 * sigma**2))
    denominator = (sigma * (2 * pi)**0.5)
    return nominator / denominator

def integrate_normal(a, b, n, mu, sigma):
    """
    Function used to determine the integral (area) of the probability density of normal distribution
    using the middle method in the interval [a, b]
    :param a: Start point of the interval [a, b]
    :param b: End point of interval [a, b]
    :param n: Number of divisions of interval [a, b]
    :param mu: Mean of the distribution
    :param sigma: Standard deviation of the distribution
    :return: Area between [a, b], output in decimals (0.4 not 40 %)
    """
    dx = float(b-a)/n
    area = 0
    midpoint = a + (dx/2)

    for i in range(n):
        area += normal(midpoint, mu, sigma) * dx
        midpoint += dx
    return area
