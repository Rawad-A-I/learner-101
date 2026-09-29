%% ELE 443 - Control Systems Lab - Fall 2026
%  Assignment 2 - Problem 6
%  Mesh analysis. Loops I1 (left) and I2 (right), both taken clockwise.
%  Branches: 1k (top-left), 3k (bottom-left), 4k (shared middle),
%            2k (top-right), 5k (bottom-right).
%  Assumption: 10V source drives I1 and 20V source drives I2, each in the
%  direction of its own loop current (adjust signs if your reading of the
%  source polarities in the figure differs).
%
%    (1k+3k+4k)*I1 -      4k*I2   = 10
%        -4k*I1   + (2k+5k+4k)*I2 = 20

clear; clc;

Rmat = [1000+3000+4000,       -4000;
              -4000,   2000+5000+4000];
Vsrc = [10; 20];

Isol = Rmat\Vsrc;
I1 = Isol(1)
I2 = Isol(2)
