
function [plate]=myOCR(directorio, archivo)

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  Escala de Grises
clc; 
%close all; Ver el funcionamiento del codigo
nroSeg=0; % tiempo de espera en segundos

% directorio='C:\Documents and Settings\Ivan Garcia\Mis documentos\Posibles Temas\Reconocimiento Placas\';
% I=imread(strcat(directorio, 'toma15.jpg'));
% info=imfinfo(strcat(directorio, 'toma15.jpg'));

I=imread(strcat(directorio, archivo));
info=imfinfo(strcat(directorio, archivo));

if (info.ColorType=='truecolor')              %Ciclo para determinar si es a color o en
    I=rgb2gray(I);                          %escala de grises para poder hacer o no la
else                                        %conversion necesaria
    I=I;
end

tam = get(0,'ScreenSize');
figure('Tag','frmGris', 'Position',  [1 tam(4)/2 tam(3)* 0.6 tam(4) * 0.6]); 
subplot(3,3,1); imshow(I); % escala de grises
title('Escala de Grises');
pause(nroSeg);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%   recorte y determinacion del umbral

[R C]=size(I);                                          %Halla el tamaño de la imagen
cropsize=[(R*0.25) (C*0.15) (C*0.625) (R*0.6)];         %Determina seccion a cortar    
Ic=imcrop(I,cropsize);                                  %Recorta la imagen para eliminar fondo innecesario
%figure; 
subplot(3,3,2); imshow(Ic)                                      %Grafica Zona recortada
title('Imagen recortada');
pause(nroSeg);
Id=double(Ic); [R C]=size(Ic);                           %Convierte imagen a doble para operaciones
%I2=sobel(Id,R,C,2.5);                                   %Halla gradiente de sobel
%umbral=umbraloptimo(Id,R,C,I2);                         %Halla umbral optimo
umbral=100;

% umbral = graythresh(Ic);		% Calcula el umbral entre [0 1]
% bw = im2bw(Ic, umbral);		% binariza la imagen con el umbral calculado
% umbral = umbral *255;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Localiza la zona de la Placa en la imagen BW

st=strel('disk',11);                     %Elemento estructurante de 10 pixeles de radio
IM2=imbothat(Ic,st);                     %Hace Bottom-Hat (baja el contraste de la imagen)
subplot(3,3,3); imshow(IM2);
title('Bottom-Hat (disk)');
I3=IM2>umbral;                           %Aplica Umbral (binariza la imagen)
subplot(3,3,4); imshow(I3);
title('Imagen Binarizada');
LH=strel('line',60,0);                   %Elemento estructurante lineal horizontal
IM3=imclose(I3,LH);                      %Closing con elemento estructurante
subplot(3,3,5); imshow(IM3);
title('BW Closing');
LV=strel('line',20,90);                  %Elemento estructurante lineal vertical
IM4=imopen(IM3,LV);                      %Hace opening con elemento estructurante 
subplot(3,3,6); imshow(IM4);
title('BW Opening');

DIV=strel('line',35,90);                 %Elemento estructurante lineal vertical
IM5=imdilate(IM4,DIV);                   %Dilata con E.E. vertical
subplot(3,3,7); imshow(IM5);
title('BW Dilate Vertical');

DIH=strel('line',20,0);                  %Elemento estrucutrante lineal horizontal
IM6=imdilate(IM5,DIH);                   %Dilata con E.E. horizontal
subplot(3,3,8); imshow(IM6);             %Muestra la zona de la placa localizada en BW
title('BW Dilate Horizontal');    
pause(nroSeg);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  ubicación de la placa y sus dimensiones 

% Segmentación basado en Regiones

L=bwlabel(IM6);                                         %Crea regiones
stats=regionprops(L,'all');                             %Estadisticas de las regiones
Idx=find([stats.Area]>(7000));                          %Diferencia las regiones con Area > 7000
IM6=ismember(L,Idx);                                    %Crea una imagen con dichas regiones

L=bwlabel(IM6);                                %Crea regiones
stats = regionprops(L,'all');                  %Estadisticas de las regiones
E=stats(1).BoundingBox;                        %Toma tamaño de la region
X=E.*[1 0 0 0]; X=max(X);              %Determina eje X esquina superior Izq. Placa
Y=E.*[0 1 0 0]; Y=max(Y);              %Determina eje Y esquina superior Der. Placa
W=E.*[0 0 1 0]; W=max(W);               %Determina Ancho Placa
H=E.*[0 0 0 1]; H=max(H);              %Determina Altura placa

%X=X-30; % para que coja la I al inicio
%W=W+30; % para que coja la I al inicio
Corte=[X Y W H];                               %Determina coordenadas de corte
IMF=imcrop(Ic,Corte);                          %Realiza el corte   
%figure;
subplot(3,3,9); imshow(IMF)                            %Muestra imagen de la zona de la placa a colores
title('Zona de Placa Localizada');
pause(nroSeg);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

umbral=120;                                             %Aplico un Umbral de 120
placa=IMF>umbral;                                       %Aplica umbral a placa
L=bwlabel(placa);                                       %Crea regiones
stats=regionprops(L,'all');                             %Estadisticas de las regiones
placadx=find([stats.Area]>(4500));                      %Diferencia las regiones con Area > 4500
placa=ismember(L,placadx);                              %Crea una imagen con dichas regiones
L=bwlabel(placa);                                       %Crea regiones
stats=regionprops(L,'all');                             %Estadisticas de las regiones
E2=stats(1).BoundingBox;                                %Toma tamaño de la region
X2=E2.*[1 0 0 0]; X2=max(X2);                  %Determina eje X esquina superior Izq. Placa
Y2=E2.*[0 1 0 0]; Y2=max(Y2);                   %Determina eje Y esquina superior Der. Placa
W2=E2.*[0 0 1 0]; W2=max(W2);                   %Determina Anchura placa
H2=E2.*[0 0 0 1]; H2=max(H2);                   %Determina Altura placa
Corte2=[X2 Y2 W2 H2];                                   %Determina coordenadas de corte
C2=imcrop(IMF,Corte2);                                  %Realiza el corte
Wx=round(W2*0.97); Hx=round(H2*0.85); %0.94/0.756
Cortex=[4 12 Wx Hx];
C2=imcrop(C2,Cortex);
figure('Tag','frmPlaca', 'Position',  [tam(3)/3 1 tam(3)* 0.6 tam(4) * 0.6]);
subplot(3,3,1); imshow(C2)                                      %Muestra Imagen
title('Imagen de la Placa');
pause(nroSeg);
%C3=C2;
st=strel('disk',16); % AUMENTADO PARA LA W                     %Elemento estructurante de 10 pixeles de radio
C3=imbothat(C2,st);
%subplot(3,3,2); imshow(C3)
umbral2=90;
C5=C3>umbral2;
subplot(3,3,2); imshow(C5);
title('Placa Binarizada');
pause(nroSeg);
L=bwlabel(C5);
stats=regionprops(L,'all');
placadx=find([stats.Area]>((W2*H2)*0.014));             %Diferencia las regiones con Area > 1.5% del area total
placa=ismember(L,placadx);                              %Crea una imagen con dichas regiones
subplot(3,3,3); imshow(placa);  % solo la placa con los 6 numeros.
title('Números y Letras de Placa');
pause(nroSeg);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%% segmentacion y dimensionamiento

L=bwlabel(placa);
stats=regionprops(L,'all');
tam_stats=size(stats)


E3=stats(1).BoundingBox;                        %Toma tamaño de la region 1, primer caracter
X3=E3.*[1 0 0 0]; X3=max(X3);                   %Determina eje X esquina superior Izq. Placa
Y3=E3.*[0 1 0 0]; Y3=max(Y3);                   %Determina eje Y esquina superior Der. Placa
W3=E3.*[0 0 1 0]; W3=max(W3);                   %Determina Anchura placa
H3=E3.*[0 0 0 1]; H3=max(H3);                   %Determina Altura placa
Corte3=[X3 Y3 W3 H3];                           %Determina coordenadas de corte
L1=imcrop(placa,Corte3);      % ojo   C2                          %Realiza el corte
L1b=imresize(L1,[42 24]);                       % Cambia el tamaño a 42x24 píxeles
L1b=(L1b==0);       							% invertir colores de imagen
%L1b=L1b>50;  % invertir imagen
subplot(3,3,4);  imshow(L1b);                                        %Muestra el primer caracter
title('Primer Caracter');
pause(nroSeg);

if tam_stats(1)>=2
    E3=stats(2).BoundingBox;                                %Toma tamaño de la region 2, segundo caracter
    X3=E3.*[1 0 0 0]; X3=max(X3);                   %Determina eje X esquina superior Izq. Placa
    Y3=E3.*[0 1 0 0]; Y3=max(Y3);                   %Determina eje Y esquina superior Der. Placa
    W3=E3.*[0 0 1 0]; W3=max(W3);                   %Determina Anchura placa
    H3=E3.*[0 0 0 1]; H3=max(H3);                   %Determina Altura placa
    Corte3=[X3 Y3 W3 H3];                                   %Determina coordenadas de corte
    L2=imcrop(placa,Corte3);                                   %Realiza el corte
    L2b=imresize(L2,[42 24]);
    L2b=L2b==0;
    subplot(3,3,5); imshow(L2b)                                        %Muestra el segundo caracter
    title('Segundo Caracter');
    pause(nroSeg);
else
    L2b=L1b; % si no hay un caracter ponga el primer encontrado 
end

if tam_stats(1)>=3
    E3=stats(3).BoundingBox;                                %Toma tamaño de la region 3, tercer caracter
    X3=E3.*[1 0 0 0]; X3=max(X3);                   %Determina eje X esquina superior Izq. Placa
    Y3=E3.*[0 1 0 0]; Y3=max(Y3);                   %Determina eje Y esquina superior Der. Placa
    W3=E3.*[0 0 1 0]; W3=max(W3);                   %Determina Anchura placa
    H3=E3.*[0 0 0 1]; H3=max(H3);                   %Determina Altura placa
    Corte3=[X3 Y3 W3 H3];                                   %Determina coordenadas de corte
    L3=imcrop(placa,Corte3);                                   %Realiza el corte
    L3b=imresize(L3,[42 24]);
    L3b=L3b==0;
    subplot(3,3,6); imshow(L3b)                                        %Muestra el tercer caracter
    title('Tercer Caracter');
    pause(nroSeg);
else
    L3b=L1b; % si no hay un caracter ponga el primer encontrado 
end

if tam_stats(1)>=4
    E3=stats(4).BoundingBox;                                %Toma tamaño de la region 4, cuarto caracter
    X3=E3.*[1 0 0 0]; X3=max(X3);                   %Determina eje X esquina superior Izq. Placa
    Y3=E3.*[0 1 0 0]; Y3=max(Y3);                   %Determina eje Y esquina superior Der. Placa
    W3=E3.*[0 0 1 0]; W3=max(W3);                   %Determina Anchura placa
    H3=E3.*[0 0 0 1]; H3=max(H3);                   %Determina Altura placa
    Corte3=[X3 Y3 W3 H3];                                   %Determina coordenadas de corte
    L4=imcrop(placa,Corte3);                                   %Realiza el corte
    L4b=imresize(L4,[42 24]);
    L4b=L4b==0;
    subplot(3,3,7); imshow(L4b)                                         %Muestra el cuarto caracter
    title('Cuarto Caracter');
    pause(nroSeg);
else
    L4b=L1b; % si no hay un caracter ponga el primer encontrado 
end

if tam_stats(1)>=5
    E3=stats(5).BoundingBox;                                %Toma tamaño de la region 5, quinto caracter
    X3=E3.*[1 0 0 0]; X3=max(X3);                   %Determina eje X esquina superior Izq. Placa
    Y3=E3.*[0 1 0 0]; Y3=max(Y3);                   %Determina eje Y esquina superior Der. Placa
    W3=E3.*[0 0 1 0]; W3=max(W3);                   %Determina Anchura placa
    H3=E3.*[0 0 0 1]; H3=max(H3);                   %Determina Altura placa
    Corte3=[X3 Y3 W3 H3];                                   %Determina coordenadas de corte
    L5=imcrop(placa,Corte3);                                   %Realiza el corte
    L5b=imresize(L5,[42 24]);
    L5b=L5b==0;
    subplot(3,3,8); imshow(L5b)                                         %Muestra el quinto caracter
    title('Quinto Caracter');
    pause(nroSeg);
else
    L5b=L1b; % si no hay un caracter ponga el primer encontrado 
end

if tam_stats(1)>=6
    E3=stats(6).BoundingBox;                                %Toma tamaño de la region 6, sexto caracter
    X3=E3.*[1 0 0 0]; X3=max(X3);                   %Determina eje X esquina superior Izq. Placa
    Y3=E3.*[0 1 0 0]; Y3=max(Y3);                   %Determina eje Y esquina superior Der. Placa
    W3=E3.*[0 0 1 0]; W3=max(W3);                   %Determina Anchura placa
    H3=E3.*[0 0 0 1]; H3=max(H3);                   %Determina Altura placa
    Corte3=[X3 Y3 W3 H3];                                   %Determina coordenadas de corte
    L6=imcrop(placa,Corte3);                                   %Realiza el corte
    L6b=imresize(L6,[42 24]);
    L6b=L6b==0;
    subplot(3,3,9); imshow(L6b);                                         %Muestra el sexto carácter
    title('Sexto Caracter');
    pause(nroSeg);
else
    L6b=L1b; % si no hay un caracter ponga el primer encontrado 
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    OCR
%dir='C:\Documents and Settings\Ivan Garcia\Mis documentos\Posibles Temas\Reconocimiento Placas\myBDDimg\';
dir= strcat(pwd, '\myBDDimg\');  % toma el directorio de trabajo y concatena con el directorio de la BDD de letras y numeros

a=imread(strcat(dir,'A.bmp')); b=imread(strcat(dir,'B.bmp')); 
c=imread(strcat(dir,'C.bmp')); d=imread(strcat(dir,'D.bmp')); 
e=imread(strcat(dir,'E.bmp')); f=imread(strcat(dir,'F.bmp')); 
g=imread(strcat(dir,'G.bmp')); h=imread(strcat(dir,'H.bmp')); 
i=imread(strcat(dir,'I.bmp')); j=imread(strcat(dir,'J.bmp')); 
k=imread(strcat(dir,'K.bmp')); l=imread(strcat(dir,'L.bmp')); 
m=imread(strcat(dir,'M.bmp')); n=imread(strcat(dir,'N.bmp')); 
o=imread(strcat(dir,'O.bmp')); p=imread(strcat(dir,'P.bmp')); 
q=imread(strcat(dir,'Q.bmp')); r=imread(strcat(dir,'R.bmp')); 
s=imread(strcat(dir,'S.bmp')); t=imread(strcat(dir,'T.bmp')); 
u=imread(strcat(dir,'U.bmp')); v=imread(strcat(dir,'V.bmp')); 
w=imread(strcat(dir,'W.bmp')); x=imread(strcat(dir,'X.bmp')); 
y=imread(strcat(dir,'Y.bmp')); z=imread(strcat(dir,'Z.bmp')); 

uno=imread(strcat(dir,'1.bmp')); dos=imread(strcat(dir,'2.bmp'));
tres=imread(strcat(dir,'3.bmp')); cuatro=imread(strcat(dir,'4.bmp'));
cinco=imread(strcat(dir,'5.bmp')); seis=imread(strcat(dir,'6.bmp'));
siete=imread(strcat(dir,'7.bmp')); ocho=imread(strcat(dir,'8.bmp'));
nueve=imread(strcat(dir,'9.bmp')); cero=imread(strcat(dir,'0.bmp'));


alfabeto=[a b c d e f g h i j k l m n o p q r s t u v w x y z];
numeral=[uno dos tres cuatro cinco seis siete ocho nueve cero];

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Divide la matriz en un determinado número de filas y columnas, donde cada celda de la matriz es
% una submatriz (imagen de letra o numero).
matricula=[L1b L2b L3b L4b L5b L6b];
ab=mat2cell(alfabeto,42,[24 24 24 24 24 24 24 24 24 24 24 24 24 24 24 24 24 24 24 24 24 24 24 24 24 24]);
numero=mat2cell(numeral,42,[24 24 24 24 24 24 24 24 24 24]);
plac=mat2cell(matricula,42,[24 24 24 24 24 24]);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Ciclo que calcula las correlaciones de las letras de la placa contra las letras del abecedario preelaborado

fila=1;
%ind=1;
while fila <= 3   % son 3 letras
    %posp=1;
    for posp=1:3    % las letras de la placa están en los 3 primeros caracteres
        plc=plac{1,posp};   % toma una letra de la placa
        pos=1;
        temp=0;
        while pos <= 26    % se recorre las 26 letras del abecedario
            temp=ab{1,pos}; % toma una letra del abecedario (A-Z)
            co=corr2(temp,plc); % calcula el coeficiente de correlación entre la letra de la placa y la letra del abecedario preelaborada
            letra(fila,pos)=co; % guarda las correlaciones en una matriz (la fila 1 para correlaciones del primer caracter, la fila 2 para el segundo caracter, y la fila 3 para el tercer caracter)
            pos=pos+1;
        end
        fila=fila+1;
        posp=posp+1;
    end
end

maxs=max(letra,[],2);   % calcula la correlación mas alta de cada fila
for ind = 1:3      % son 3 letras
    [posx posy]=find(letra==maxs(ind,1));   % busca la fila y la columna de la correlación mas alta
    letras(ind)=posy;   % guarda la posición de la correlación mas alta en el arreglo letras
    ind=ind+1;
end

% Ciclo que calcula las correlaciones de los números de la placa contra los números preelaborados
fila=1;
while fila <= 3 % son 3 números 
    for posp=4:6        % los numeros de la placa están en los 3 ultimos caracteres
        plc=plac{1,posp};   % toma un número de la placa
        pos=1;
        temp=0;
        while pos <= 10 % se recorre los 10 dígitos
            temp=numero{1,pos}; % toma un número de los dígitos (0-9)
            co=corr2(temp,plc); % calcula el coeficiente de correlación entre un número de la placa y un número de los dígitos preelaborados
            num(fila,pos)=co;   % guarda las correlaciones en una matriz (la fila 1 para correlaciones del primer número, la fila 2 para el segundo número, y la fila 3 para el tercer número)
            pos=pos+1;
        end
        fila=fila+1;
        posp=posp+1;
    end
end

maxs=max(num,[],2); % calcula la correlación mas alta de cada fila
for ind = 1:3   % son 3 números
    [posx posy]=find(num==maxs(ind,1)); % busca la fila y la columna de la correlación mas alta
    nums(ind)=posy; % guarda la posición de la correlación mas alta en el arreglo nums
    ind=ind+1;
end

% Asigna la letra que corresponde a cada índice del arreglo letras.
    for lt = 1:3    % son 3 letras
        if letras(lt)== 1
            car(lt)='A';
        elseif letras(lt) == 2
            car(lt)='B';
        elseif letras(lt) == 3
            car(lt)='C'; 
        elseif letras(lt) == 4
            car(lt)='D';
        elseif letras(lt) == 5
            car(lt)='E';
        elseif letras(lt) == 6
            car(lt)='F';
        elseif letras(lt) == 7
            car(lt)='G';
        elseif letras(lt) == 8
            car(lt)='H';        
        elseif letras(lt) == 9
            car(lt)='I';
        elseif letras(lt) == 10
            car(lt)='J';
        elseif letras(lt) == 11
            car(lt)='K';
        elseif letras(lt) == 12
            car(lt)='L';
        elseif letras(lt) == 13
            car(lt)='M';
        elseif letras(lt) == 14
            car(lt)='N';
        elseif letras(lt) == 15
            car(lt)='O';
        elseif letras(lt) == 16
            car(lt)='P';
        elseif letras(lt) == 17
            car(lt)='Q';
        elseif letras(lt) == 18
            car(lt)='R';
        elseif letras(lt) == 19
            car(lt)='S';
        elseif letras(lt) == 20
            car(lt)='T';
        elseif letras(lt) == 21
            car(lt)='U';
        elseif letras(lt) == 22
            car(lt)='V';
        elseif letras(lt) == 23
            car(lt)='W';
        elseif letras(lt) == 24
            car(lt)='X';
        elseif letras(lt) == 25
            car(lt)='Y';
        elseif letras(lt) == 26
            car(lt)='Z';
        else
            car(lt)='*';    
        end
        lt=lt+1;
    end

    % Asigna el número que corresponde a cada índice del arreglo nums.
    for nm = 1:3   % son 3 números
        if nums(nm)== 1
            dig(nm)='1';
        elseif nums(nm) == 2
            dig(nm)='2';
        elseif nums(nm) == 3
            dig(nm)='3';
        elseif nums(nm) == 4
            dig(nm)='4';
        elseif nums(nm) == 5
            dig(nm)='5';
        elseif nums(nm) == 6
            dig(nm)='6';
        elseif nums(nm) == 7
            dig(nm)='7';
        elseif nums(nm) == 8
            dig(nm)='8';
        elseif nums(nm) == 9
            dig(nm)='9';
        elseif nums(nm) == 10
            dig(nm)='0';
        else  
            dig(nm)='*';
        end
        nm=nm+1;
    end


%close all;
plate=horzcat(car,dig); % concatena las 3 letras con los 3 números de la placa
clc;
disp('La placa reconocida es: ');
disp(plate);

return;
