function pinon()
    clc;
    g=imread('p.png');
    if size(g,3)==3     % es RGB?
       g = rgb2gray(g); 
    end
    subplot (2,2,1); imshow(g)

    bw = g > 128;   % binarizamos
    bw = ~bw; % The objects have that be white background, 
    bw=imfill(bw, 'holes');
    subplot (2,2,2); imshow(bw)

    se=strel('disk',20); % crea elemento estructurante
    bw2 = imopen(bw,se);   % apertura
    subplot (2,2,3); imshow(bw2)
    
    J=imsubtract(bw, bw2);  % bw - bw2 
    subplot (2,2,4); imshow(J)
    [L, num]=bwlabel(J);

    strcat('Numero de dientes del piñon:', sprintf('%d', num))
end

