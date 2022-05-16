function dibujar()    
%% dibuja el boundingBox y Centroide de cada region etiquetada

clc;
    % captura
    g=imread('llaves.png');
    
    % preprocesamiento
    if size(g,3)==3     % es RGB?
       g = rgb2gray(g); 
    end
    
    % segmentación
    T = graythresh(g); % Calcula el umbral entre [0 1] con m?todo Otsu
    bw = imbinarize(g, T);   % binariza
    
    bw = ~bw;
    imshow(bw)
      
    [L, n]=bwlabel(bw);
    
    % descripcion
    stats = regionprops (L, {'BoundingBox','Centroid'});
   
    % dibuja el BoundingBox y Centroide
     hold on
    for i=1:n
        rect = stats(i).BoundingBox;
        cent = stats(i).Centroid;
        rectangle('Position',rect, 'EdgeColor','g')
        plot(cent(1), cent(2),'+r')
        title(['Existen:  ', num2str(i), ' objects']);
    end
    hold off
end
