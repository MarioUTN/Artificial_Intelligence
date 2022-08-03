%% Ejercicio 01
clear all; clc;
img = imread('pastillas.jpg');
img=rgb2gray(img);
bw = edge(img,'canny');
imshow(img)
% Encuentra todos los círculos con píxeles de radio en el rango [15, 30].r
[centers, radii, metric] = imfindcircles(bw, [200 500]);

% Dibuje los cinco perímetros de círculo más fuertes sobre la imagen original.
viscircles(centers, radii,'EdgeColor','r');
sprintf('circulos: %d', length(radii))

%% Ejercicio 2
clear all; clc
img = imread('pastillas.jpg');
imshow(img)
img=rgb2gray(img);
img=imbinarize(img);
img=~img;
bw = edge(img,'canny');
imshow(img)
% Encuentra todos los círculos con píxeles de radio en el rango [15, 30].r
[centers, radii, metric] = imfindcircles(bw, [200 500]);

% Dibuje los cinco perímetros de círculo más fuertes sobre la imagen original.
viscircles(centers, radii,'EdgeColor','r');
sprintf('circulos: %d', length(radii))

%% Ejercicio 3 Eyes Detect
clear all; clc
img = imread('pastillas.jpg');
imshow(img)
img=rgb2gray(img);
img=imbinarize(img);
img=~img;
bw = edge(img,'canny');
imshow(img)
% Encuentra todos los círculos con píxeles de radio en el rango [15, 30].r
[centers, radii, metric] = imfindcircles(bw, [200 500]);

% Dibuje los cinco perímetros de círculo más fuertes sobre la imagen original.
viscircles(centers, radii,'EdgeColor','r');
sprintf('circulos: %d', length(radii))
