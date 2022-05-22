%  gradienteSobel=Sobel(imagen, filasImagen, columnasImagen, X_Porciento);

function gradienteSobel=Sobel(imagen, filasImagen, columnasImagen, X_Porciento)

% Kernel Sobel para calcular el gradiente en la direccion horizontal.
kernel=(1/8)*[-1 0 1; -2 0 2; -1 0 1];

gradiente=filtro(imagen, filasImagen, columnasImagen, kernel);

% Calculo del umbral para clasificar la respuesta del Sobel, este es tal que
% solo un X% de los gradientes van a superar el umbral.
moduloGradiente=abs(gradiente(:));
maximoModuloGradiente=round(max(moduloGradiente));
minimoModuloGradiente=round(min(moduloGradiente));
nivelesGradiente=maximoModuloGradiente-minimoModuloGradiente;
histogramaGradiente=hist(moduloGradiente, nivelesGradiente);
histogramaGradienteAcumulado=cumsum(histogramaGradiente);
umbralSobel=nivelesGradiente;
while (umbralSobel > 0)&(histogramaGradienteAcumulado(umbralSobel) > (filasImagen*columnasImagen*(1-(X_Porciento/100))))
     umbralSobel=umbralSobel-1;
end
umbralSobel=minimoModuloGradiente+umbralSobel;

% Clasificacion de la respuesta del Sobel en 1, 0 o -1.
gradienteSobel=[];
for i=1:filasImagen
   for j=1:columnasImagen
      if gradiente(i,j) > umbralSobel
      	gradienteSobel(i,j)=1;
      else
        if gradiente(i,j) < -umbralSobel
      	  gradienteSobel(i,j)=-1;
        else
      	  gradienteSobel(i,j)=0;
      	end
      end
   end
end

return;