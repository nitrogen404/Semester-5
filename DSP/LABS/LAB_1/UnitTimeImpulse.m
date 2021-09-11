% Discreate time sequence for UNIT IMPULSE SIGNAL
clc; 
clear all; 
close all; 
t = -2:1:2; 
y = [zeros(1,2),ones(1,1),zeros(1,2)]; 
subplot(3,2,1); 
stem(t,y); 
ylabel('Amplitude'); 
xlabel('(a)n'); 
title('Unit Impulse Signal');

