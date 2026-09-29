%% ELE 443 - Control Systems Lab - Fall 2026
%  Assignment 2 - Problem 1

clear; clc;

A = randi([7,17],3,3)                  % 3x3 matrix, random integers in [7,17]

detA = det(A)                          % a. determinant
rankA = rank(A)                        % b. rank
R = rref(A)                            % c. reduced row echelon form

[V,D] = eig(A);                        % d. eigenvectors (V) and eigenvalues (D)
V
D

normsV = vecnorm(V)                    % e. norm of each eigenvector (each column of V)

check = A*V - V*D                      % f. sanity check: should be ~0 (numerical noise)

EBE = exp(A)                           % g. element-by-element exponential
Emat = expm(A)                         %    matrix exponential
