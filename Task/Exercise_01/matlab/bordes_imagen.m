%% Detectar bordes canny
clear all; clc;
I=imread('imagen_line.jpeg');  % lee la imagen
% preprocesamiento
I=rgb2gray(I)  % escala de grises
subplot (2,2,1); imshow(I)  % muestra la imagen
%I = I > 128   % binariza (umbral fijo)
%I = graythresh(I)   % binariza (umbral fijo)
%subplot (1,2,1); imshow(I)  % muestra la imagen
bw = edge(I, 'canny')
subplot (2,2,2); imshow(bw)  % muestra la imagen

%% Detectar bordes sobel
clear all; clc;
I=imread('imagen_line.jpeg');  % lee la imagen
% preprocesamiento
I=rgb2gray(I)  % escala de grises
subplot (2,2,1); imshow(I)  % muestra la imagen
%I = I > 128   % binariza (umbral fijo)
%I = graythresh(I)   % binariza (umbral fijo)
%subplot (1,2,1); imshow(I)  % muestra la imagen
bw = edge(I, 'sobel')
subplot (2,2,2); imshow(bw)  % muestra la imagen

%% Detectar bordes Prewitt
clear all; clc;
I=imread('imagen_line.jpeg');  % lee la imagen
% preprocesamiento
I=rgb2gray(I)  % escala de grises
subplot (2,2,1); imshow(I)  % muestra la imagen
%I = I > 128   % binariza (umbral fijo)
%I = graythresh(I)   % binariza (umbral fijo)
%subplot (1,2,1); imshow(I)  % muestra la imagen
bw = edge(I, 'Prewitt')
subplot (2,2,2); imshow(bw)  % muestra la imagen

stats = regionprops(bw,'area')

%% Detectar bordes Roberts
clear all; clc;
I=imread('imagen_line.jpeg');  % lee la imagen
% preprocesamiento
I=rgb2gray(I)  % escala de grises
subplot (2,2,1); imshow(I)  % muestra la imagen
%I = I > 128   % binariza (umbral fijo)
%I = graythresh(I)   % binariza (umbral fijo)
%subplot (1,2,1); imshow(I)  % muestra la imagen
bw = edge(I, 'Roberts')
subplot (2,2,2); imshow(bw)  % muestra la imagen
