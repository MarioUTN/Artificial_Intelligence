% Escalamiento
% I = imread('0.bmp');
% K = imresize(I, 2, 'bilinear');
% imtool(K)
% K = imresize(I, 0.5, 'bicubic');
% imshow(K)

% rotación
% I = imread('0.bmp');
% imtool(I)
% K = imrotate(I, 35, 'bilinear');
% imtool(K)
% K = imrotate (I, 90, 'bicubic');
% imtool(K)

% correlación
I=imread('B.bmp');
J=imread('8.bmp');
k=corr2(I, J)

% histograma
% I=imread('F:\Mis Documentos\UTN\Docencia\Abr-Jul 2017\IA\e-libro\Libro\Imagenes por Capitulos\5\figura 5-3a.jpg');
% I = rgb2gray(I);
% imhist(I)
% J=imadjust(I);
% imhist(J)
% imtool(J)
