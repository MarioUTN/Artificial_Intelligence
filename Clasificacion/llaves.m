function llaves()
    clc;
    % captura
    g=imread('llaves.png');
    
    % preprocesamiento
    if size(g,3)==3     % es RGB?
       g = rgb2gray(g); 
    end
    subplot (2,2,1); imshow(g)

    % segmentacion
     bw = g > 128;   % binarizamos
%     T = graythresh(g); % Calcula el umbral entre [0 1] con m?todo Otsu
%     bw = im2bw(g, T);   % binariza
    
    bw = ~bw;
    subplot (2,2,2); imshow(bw)
    
    % eliminamos cierto ruido, puntos aislados
    se=strel('square',1); % crea elemento estructural
    J = imopen(bw,se);   % cierre
    subplot (2,2,3); imshow(J)
    
    % segmentacion
    [L, num]=bwlabel(J);
    
    % descripcion
    stats = regionprops (L, 'EulerNumber');
   
    % clasificacion
%     num_euler = cat(1, stats.EulerNumber);
    num_euler = [stats.EulerNumber];
    boca=sum(num_euler == 1); % euler = #objetos - #agujeros
    corona=sum(num_euler == -1);
    strcat('Llaves de Corona:', sprintf('%d', corona))
    strcat('Llaves de Boca:', sprintf('%d', boca))
%     return
    
    % Opcional. Dibujar las llaves de cada tipo (boca, corona)
    L1 = L;
    L2 = L;
    for i = 1:length(stats)
        if stats(i).EulerNumber == -1 
            L1(L1==i)=0; % elimina las de corona
        elseif (stats(i).EulerNumber == 1) 
            L2(L2==i)=0; % elimina las de boca
        end
    end

    subplot(2,2,3),imshow(L1); title(strcat('boca:', num2str(boca)))
    subplot(2,2,4),imshow(L2); title(strcat('corona:', num2str(corona)))
end

