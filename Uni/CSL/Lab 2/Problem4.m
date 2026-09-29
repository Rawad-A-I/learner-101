clear; clc;

syms n

x4a_sym = symsum(4*(-1)^(n-1)/(2*n-1), n, 1, Inf);   % a. Leibniz series -> pi
x4a_sym = simplify(x4a_sym)
pretty(x4a_sym)                                      %    readable textbook-style formatting
x4a = double(x4a_sym)

y4b_sym = symsum(1/gamma(n+1), n, 0, Inf)            % b. sum 1/n! -> e
pretty(y4b_sym)                                      %    readable textbook-style formatting
y4b = double(y4b_sym)
