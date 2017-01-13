#! /usr/bin/python
# -*- coding: utf-8 -*-
u"""
author: Atsushi Sakai
"""
import numpy as np


def solve_qp_with_ep_const(P, q, A, b):
    """
    solve quadratic programming with only equality constraints
          min 0.5*x*P*x + q.T*x
          s.t Ax = b
    """
    K1 = np.concatenate((P, A.T), axis=1)
    K2 = np.concatenate((A, np.zeros((A.shape[0], A.shape[0]))), axis=1)
    K = np.concatenate((K1, K2), axis=0)
    d = np.concatenate((-q.T, b), axis=0)
    star = np.linalg.solve(K, d)
    x_star = star[0:A.shape[1], :]
    return x_star


def test_solve_qp_with_ep_const():
    print("start test_solve_qp_with_ep_const")
    P = np.matrix(np.diag([1.0, 0.0]))
    q = np.matrix(np.array([3.0, 4.0]))
    A = np.matrix([1.0, 1.0])
    b = np.matrix(1.0)
    print("P")
    print(P)
    print("q")
    print(q)
    print("A")
    print(A)
    print("b")
    print(b)

    x = solve_qp_with_ep_const(P, q, A, b)
    print("x")
    print(x)

    assert x[0] - 1.0 < 0.0001
    assert x[1] - 0.0 < 0.0001

    print("finish test_solve_qp_with_ep_const")


def test():
    test_solve_qp_with_ep_const()

if __name__ == '__main__':
    test()
