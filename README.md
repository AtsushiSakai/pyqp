# pyqp
[![Build Status](https://travis-ci.org/AtsushiSakai/pyqp.svg?branch=master)](https://travis-ci.org/AtsushiSakai/pyqp)
[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE)

Simple convex quadratic programming solver

## Description

This is a simple and light-weight convex quadratic programming (QP) solver.

It only uses numpy and it is distributed as a single python file module.


## Install

Download this repository and import pyqp.py

## Usage

## solve_qp_with_ep_const

![1](https://github.com/AtsushiSakai/pyqp/blob/master/images/1.png)

This function solves convex QP with only equallity constraints.

usage:

```python
P = np.matrix(np.diag([1.0, 0.0]))
q = np.matrix(np.array([3.0, 4.0]))
A = np.matrix([1.0, 1.0])
x = solve_qp_with_ep_const(P, q, A, b)
print(x)
```

See the test code in pyqp.py.

## Requirement

- numpy

## Licence

[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)

## Author

[AtsushiSakai](https://github.com/AtsushiSakai)


