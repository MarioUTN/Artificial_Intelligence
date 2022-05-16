%%
function morfologia1
    % elimina las lineas de la imagen y deja solo los circulos
    clc;    % limpia la ventana de comandos
    % captura
    I=imread('imagen_line.jpeg');  % lee la imagen
    % preprocesamiento
    I=rgb2gray(I)  % escala de grises
    I = I > 128   % binariza (umbral fijo)
    %I = graythresh(I)   % binariza (umbral fijo)
    subplot (1,2,1); imshow(I)  % muestra la imagen
    
    % morfologia matematica
    se1=strel('line',20,0) % crea elemento estructural tipo disco
    J1 = imopen(I,se1); % apertura, elimina objetos que no se ajustan al patron de disco
    % Segmentacion
    subplot (2,2,1); imshow(J1);
    [L, num1]=bwlabel(J1)   % etiquetado de componentes
    title(strcat('Lines 01: ', num2str(num1)));  % pone un titulo
    
    
    se2=strel('line',20,45)
    J2 = imopen(I,se2);
    subplot (2,2,2); imshow(J2)
    [L, num2]=bwlabel(J2)
    title(strcat('Lines 02: ', num2str(num2)));
    
    se3=strel('line',20,315)
    J3 = imopen(I,se3);
    subplot (2,2,3); imshow(J3)
    [L, num3]=bwlabel(J3)    
    title(strcat('Lines 03: ', num2str(num3)));
    
    se4=strel('line',20,90)
    J4 = imopen(I,se4);
    subplot (2,2,4); imshow(J4)
    [L, num4]=bwlabel(J4)    
    title(strcat('Lines 04: ', num2str(num4)));
end

% Ver ayudas, ejecutar el codigo paso a paso, line 13
% Trabajo autonomo 
% (Open CV) Libreria a usar
% Pasar a python todas las actividades realizadas en clases
% leer hasta el cap 7
