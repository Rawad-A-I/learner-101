%% ELE 443 - Control Systems Lab - Fall 2026
%  Assignment 2 - Problem 5

clear; clc;

syms t s lambda a b positive

f = lambda*exp(-lambda*t);
F = laplace(f, t, s)                   % a. Laplace transform of f(t)
pretty(F)                              %    readable textbook-style formatting

g = cos(a*t)*exp(-b*t);
G = laplace(g, t, s)                   % b. Laplace transform of g(t)
pretty(G)                              %    readable textbook-style formatting

sF = s*F;
sG = s*G;

sF_at_0   = subs(sF, s, 0)             % c. sF(s) and sG(s) at s = 0 and s = infinity
sF_at_inf = limit(sF, s, Inf)
sG_at_0   = subs(sG, s, 0)
sG_at_inf = limit(sG, s, Inf)
