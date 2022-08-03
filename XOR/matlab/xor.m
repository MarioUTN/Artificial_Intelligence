%% Function XOR
clear all; clc;

net = newff([0 1; 0 1],[2 1],{'logsig','logsig'})
input = [1 1 0 0; 1 0 1 0]
output=sim(net,input)
target = [0 1 1 0]
plot(target, 'o') 
hold on 
plot(output, '+r') 
net.IW{1,1}
net.IW{1,1}(1,2)=5; 
net.IW{1,1}
net.LW{2,1}
output=sim(net,input)
plot(output,'g*')
net = train(net,input,target);
output = sim(net,input)
net.IW{1,1}
net.LW{2,1}
 
