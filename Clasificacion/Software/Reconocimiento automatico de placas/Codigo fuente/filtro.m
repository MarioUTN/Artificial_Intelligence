% Tratamiento de Imagenes por Computadora
% RecAM (Reconocimiento Automático de Matrículas)
% Version 1.0
% Rodrigo Abal Soneira <rabal@adinet.com.uy>
% Raul Medeglia <raumed@adinet.com.uy>
% Nicolas Pebet <npebet@adinet.com.uy>
% 7.07.2003
%
%    imagenFiltrada=Filtro(imagen, filasImagen, columnasImagen, kernel);

% Este algoritmo esta implementado para optimizar operaciones con kernel's de 3x3.

function imagenFiltrada=Filtro(imagen, filasImagen, columnasImagen, kernel)

T=[0 0 1;0 1 0;1 0 0];
kernelRotado=T*kernel*T;

imagenFiltrada=zeros(filasImagen, columnasImagen);

for i=1+1:filasImagen-1
   for j=1+1:columnasImagen-1
      imagenFiltrada(i,j)=sum(sum(imagen(i-1:i+1,j-1:j+1).*kernelRotado));
   end
end

