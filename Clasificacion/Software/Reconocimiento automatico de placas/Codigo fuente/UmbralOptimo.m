%    umbral=UmbralOptimo(imagen, filasImagen, columnasImagen, gradiente);

% Algoritmo para calcular el umbral optimo para la binarizacion.

function umbral=UmbralOptimo(imagen, filasImagen, columnasImagen, gradiente)

% Creo una variable que me dice de que color era el ultimo grupo que guarde
% de esta forma se que la cola del final de la fila pertenece al otro color
% la variable se llama ultimoColor, si vale cero fue oscuro y si vale uno
% fue claro.

numOscuros=0;
numClaros=0;
oscuros=0;
claros=0;
cont=0;
acum=0;

% Este if es para solucionar el problema que ocurre si no hay bordes en la
% primer fila entonces no se sabe si es clara o oscura.
% Supongo continuidad en los colores, si en la segunda fila tampoco hay bordes
% estos los supongo del mismo color que la primera.

if imagen(1,1)<(max(max(imagen))/2)
  % Como es oscuro pongo que el ultimo color fue claro.
  ultimoColor=1;
else
  % Como es claro pongo que el ultimo color fue oscuro.
  ultimoColor=0;
end

for i=1:filasImagen
   if ultimoColor==0
     numClaros=numClaros+cont;
     cont=0;
     claros=claros+acum;
     acum=0;
   else
     numOscuros=numOscuros+cont;
     cont=0;
     oscuros=oscuros+acum;
     acum=0;
   end
   for j=1:columnasImagen
      if gradiente(i,j)==0
      	cont=cont+1;
      	acum=acum+imagen(i,j);
      else
           if gradiente(i,j)==-1
             numOscuros=numOscuros+cont;
      	     cont=1;
      	     oscuros=oscuros+acum;
      	     acum=imagen(i,j);
      	     ultimoColor=0;
      	   else
      	     numClaros=numClaros+cont;
      	     cont=1;
      	     claros=claros+acum;
      	     acum=imagen(i,j);
      	     ultimoColor=1;
      	   end
      end
   end
end

if ultimoColor==0
  numClaros=numClaros+cont;
  claros=claros+acum;
else
  numOscuros=numOscuros+cont;
  oscuros=oscuros+acum;
end

% Media de los claros.
mediaClaros=claros/numClaros;

% Media de los oscuros.
mediaOscuros=oscuros/numOscuros;

% Umbral optimo para la binarizacion.
umbral=(mediaOscuros*numClaros+mediaClaros*numOscuros)/(numClaros+numOscuros);

return;
