#! /usr/bin/python3.3


class Polynom(object):

    def __init__(self, ai):
        self.ai = ai

    def get_polynom(self, x):
        return sum((k * (x ** z) for z, k in enumerate(self.ai)))

    def get_derivate(self, x):
        return sum(((x ** i) * (i + 1) * self.ai[i + 1] for i in range(len(self.ai) - 1)))

    def bisection_method(self, a, b, e):
        c = (a + b) / 2
        i = 0
        while (abs(a - b) > e):
            print(abs(a - b), " > ", e)
            print("#", i, "current result = ", c)
            # print("#", i, "interval: [" , a, ",", b, "]")
            if (self.get_polynom(a) * self.get_polynom(c) <= 0):
                b = c
            else:
                a = c
            c = (a + b) / 2
            i += 1
        return c

    def chord_method(self, a, b, e):
        i = 0
        c = (a * self.get_polynom(b) - b * self.get_polynom(a)) / \
            (self.get_polynom(b) - self.get_polynom(a))
        c_prev = 100000
        while ((abs(c - c_prev) >= e) or abs(self.get_polynom(c)) >= e):
            # print("#", i, "interval: [" , a, ",", b, "]")
            print("#", i, "current result = ", c)
            print(abs(c - c_prev), " > ", e, "   or   ",
                  abs(self.get_polynom(c)), ">=", e)

            if (self.get_polynom(a) * self.get_polynom(c) <= 0):
                b = c
            else:
                a = c
            c_prev = c
            c = (a * self.get_polynom(b) - b * self.get_polynom(a)) / \
                (self.get_polynom(b) - self.get_polynom(a))
            i += 1
        return c

    def Newton_method(self, xk, e):
        i = 0
        xk_1 = xk - self.get_polynom(xk) / self.get_derivate(xk)
        while ((abs(xk - xk_1) >= e) or (abs(self.get_polynom(xk)) >= e)):
            print("#", i, "current result = ", xk_1)
            print(abs(xk - xk_1), " >= ", e, "   or   ",
                  abs(self.get_polynom(xk)), ">=", e, '\n')
            xk = xk_1
            xk_1 = xk - self.get_polynom(xk) / self.get_derivate(xk)
            i += 1
        return xk_1


def main():
    print("NCM: Assignment #1: Solving nonlinear equations \n")

    pol = Polynom([-4, -2, 1, -3, 1])
    a = 0.067
    # a = -2.5
    b = 5
    # b = -0.57
    e = 0.00001

    print("====================Chord_method==========================")
    print(pol.chord_method(a, b, e), '\n')

    print("====================Bisection method==========================")
    print("Bisection_method: ", pol.bisection_method(a, b, e), '\n')

    print("====================Newton method==========================")
    print("Newton_method: ", pol.Newton_method(b, e), '\n')


if __name__ == '__main__':
    main()