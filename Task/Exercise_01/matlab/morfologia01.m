%%
function morfologia1
    % elimina las lineas de la imagen y deja solo los circulos
    clc;    % limpia la ventana de comandos
    % captura
    I=imread('morfologia.jpeg');  % lee la imagen
    % preprocesamiento
    I=rgb2gray(I);  % escala de grises
    I = I > 64;    % binariza (umbral fijo)
    subplot (1,2,1); imshow(I)  % muestra la imagen
    % morfologia matematica
    se=strel('diamond',5); % crea elemento estructural tipo disco
    J = imopen(I,se);   % apertura, elimina objetos que no se ajustan al patron de disco
    subplot (1,2,2); imshow(J);
    % segmentacion
    [L, num]=bwlabel(J);   % etiquetado de componentes
    title(strcat('Puntos: ', num2str(num)));  % pone un titulo
end

% Ver ayudas, ejecutar el codigo paso a paso, line 13
