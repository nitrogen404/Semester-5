n=input('enter the length of exponential sequence ') ; 
t=0:n ; 
a=input('enter the value of a ') ; 
y=exp(a*t) ; 
subplot(3,2,4) ; 
stem(t,y) ; 
ylabel('Amplitude') ; 
xlabel('(d)n ') ; 
title('Exponentail Sequence') ;