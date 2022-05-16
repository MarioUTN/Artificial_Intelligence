%% Exercise of Artificial Intelligence
% imagen
I = imread('grifinho.png');
imshow(I);
% convertir a imagen RGB
hsv_image = rgb2hsv(I);
I=rgb2gray(hsv_image);
j=imadjust(I);
figure; imhist(j)

%% video
myVideo = VideoReader('mejores_goles.mp4');
while hasFrame(myVideo)
img = readFrame(myVideo);
imshow(img)
end
%% webcam
cam = webcam(1); % instale usbwebcams.mlpkginstall
preview(cam);
img = snapshot(cam);
image(img);
