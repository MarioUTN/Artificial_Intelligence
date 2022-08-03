function cancer()
    clc
    % Classification problem
    % URL: http://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Diagnostic%29
    bcdata=csvread('wdbc2.data.csv', 0, 0)
    % reads data from the file starting at row offset R1 and column offset C1.
    size(bcdata) % 569x31
    bcdata=bcdata';
    size(bcdata) % 31x569

    target=bcdata(1,:); % The first column is the ground truth (output)
    size(target)
    % Malignant=1, Benign=0
    indata=bcdata(2:31,:); % 30 attributes (input)
    input_ranges=minmax(indata);
    
    net=newff(input_ranges,[30 1],{'logsig','logsig'},'trainlm'); % optimization method: Levenberg-Manquardt
   
    training_in = indata(:,1:2:length(indata)); %  50% training set
    training_target = target(1:2:length(target)); % 
    % struct
    testset.P = indata(:,2:2:length(indata)); %  50%, test set (P=predictors, T=tarjet)
    testset.T = target(2:2:length(target));
    
    net.trainParam.show=1; % show iteration data
    net=train(net,training_in,training_target,[],[],testset);
    porc_err_entren = 100*(1-accuracy(net,training_in,training_target))
    porc_err_validac = 100*(1-accuracy(net,testset.P,testset.T)) % predictors, tarjet
    porc_err_validac = 100*(1-accuracy2(net,testset.P,testset.T)) % predictors, tarjet
    porc_err_todo = 100*(1-accuracy(net,indata,target))
    
    % simulacion
    y_pred=round(sim(net,testset.P(:,2))) %patient #2
    y_true=testset.T(:,2) %patient #2
    
    y_pred=round(sim(net,testset.P(:,11))) %patient #11
    y_true=testset.T(:,11) %patient #11
end

function return_value = accuracy(net,input,target)
    output=sim(net,input); % predicted values
    correct=0;
    for i=1:length(output)
	   % tarjet: ground truth (etiquetas)
	   % output: predicted values from model
        if ((target(i)==1) && (output(i)>=0.5))
            correct=correct+1; % true positive
        elseif ((target(i)==0) && (output(i)<0.5))
            correct=correct+1; % true negative
        end
    end
    return_value = correct./length(output); % (TP+TN)/total
end

% otra funcion similar más concreta para medir la exactitud
function return_value = accuracy2(net,input,target)
   output=sim(net,input); % predicted values
   output= round(output);
   accuracy = mean(output == target); % vectorizacion
   return_value = accuracy;
end
