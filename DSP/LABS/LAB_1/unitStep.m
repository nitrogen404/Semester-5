n=input('enter the N value '); 
t=0:1:n-1; 
y=ones(1,n); 
subplot(3,2,2); 
stem(t,y); 
ylabel('Amplitude'); 
xlabel('(b)n') ; 
title('Unit Step Sequence') ;