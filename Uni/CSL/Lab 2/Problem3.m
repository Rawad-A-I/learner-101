clear; clc;

syms t x

I3a = int(1/(1+t^2), t)                                         

I3b_sym = int(exp(-x^2/2), x, -1, 1); 
I3b = double(I3b_sym)                  
