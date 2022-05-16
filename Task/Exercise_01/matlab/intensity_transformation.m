% https://docs.opencv.org/3.4/d5/daf/tutorial_py_histogram_equalization.html
% histogram equalization is used to improve the contrast of our images.
% This is useful in many cases. For example, in face recognition, before 
% training the face data, the images of faces are histogram equalized to make
% them all with same lighting conditions.
% cv.equalizeHist()
% Histogram equalization is good when histogram of the image is confined to 
% a particular region. It won't work good in places where there is large 
% intensity variations where histogram covers a large region, ie both bright 
% and dark pixels are present.

%% input
clc
close all
fil = 2, col = 2;
I = imread('imagen.jpeg');
f = rgb2gray(I);
figure, subplot(fil, col,1), imshow(f)
title('original')
subplot(fil,col,2), imhist(f)
% subplot(fil,col,3), edge(f,'Canny');
% level = graythresh(f);
% subplot(fil,col,4), im2bw(f, level);

%% adapt histeq
g= adapthisteq(f, 'NumTiles', [25 25], 'ClipLimit', 0.05);
subplot(fil,col,3), imshow(g)
title('adapthisteq')
subplot(fil,col,4), imhist(g)
pause
% subplot(fil,col,7), edge(g,'Canny');
% level = graythresh(g);
% subplot(fil,col,8), im2bw(g, level);

%% histeq
g= histeq(f, 256);
subplot(fil,col,3), imshow(g)
title('histeq')
subplot(fil,col,4), imhist(g)
pause
% subplot(fil,col,7), edge(g,'Canny');
% level = graythresh(g);
% subplot(fil,col,8), im2bw(g, level);

%% stretching
g= intrans(f, 'stretch', mean2(tofloat(f)),0.9);
subplot(fil,col,3), imshow(g)
title('stretching')
subplot(fil,col,4), imhist(g)
pause
% subplot(fil,col,7), edge(g,'Canny');
% level = graythresh(g);
% subplot(fil,col,8), im2bw(g, level);

%% imadjust
g=imadjust(f, stretchlim(f), []);
subplot(fil,col,3), imshow(g)
title('imadjust')
subplot(fil,col,4), imhist(g)
pause
% subplot(fil,col,7), edge(g,'Canny');
% level = graythresh(g);
% subplot(fil,col,8), im2bw(g, level);

%% imadjust adversed
g=imadjust(f, stretchlim(f), [1 0]);
subplot(fil,col,3), imshow(g)
title('imadjust reversed')
subplot(fil,col,4), imhist(g)
% subplot(fil,col,7), edge(g,'Canny');
% level = graythresh(g);
% subplot(fil,col,8), im2bw(g, level);


