clear; clc;

syms y(t)
Dy = diff(y,t);
ode = diff(y,t,2) - 6*diff(y,t) + 2*y == exp(t);
cond1 = y(0) == 4;
cond2 = Dy(0) == 5;
ySol(t) = dsolve(ode, [cond1, cond2]);
ySol = simplify(ySol)

pretty(ySol)                           % readable textbook-style formatting
