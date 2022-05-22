function orientacion_img()
    clc;
    % captura
    g=imread('pieza-1.png'); % Read the image
    
    % preprocesamiento
    if size(g,3)==3     % es RGB? % if is of 3 dimentions -> converter
       g = rgb2gray(g); 
    end
    subplot (2,2,1); imshow(g)
    
    % segmentaci?n
    umbral = graythresh(g); % Otsu
    bw=im2bw(g, umbral);
    subplot (2,2,2); imshow(bw)
    
    bw2 = imfill (bw, 'holes'); % rellenar el objeto
    subplot (2,2,3); imshow(bw2)
    
    % descripcion
    stats = regionprops (bw2, 'orientation');
    ang = stats(1).Orientation;
    Ir = imrotate(bw, -ang);
    %Ir = imrotate(g, -stats(1).Orientation, 'bilinear');
    subplot (2,2,4); imshow(Ir);
    
    title(strcat('Rotada: ', num2str(-stats(1).Orientation)));
end

