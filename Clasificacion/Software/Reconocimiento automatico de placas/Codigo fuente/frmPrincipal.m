
function varargout = frmPrincipal(varargin)
% FRMPRINCIPAL M-file for frmPrincipal.fig
%      FRMPRINCIPAL, by itself, creates a new FRMPRINCIPAL or raises the existing
%      singleton*.
%
%      H = FRMPRINCIPAL returns the handle to a new FRMPRINCIPAL or the handle to
%      the existing singleton*.
%
%      FRMPRINCIPAL('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in FRMPRINCIPAL.M with the given input arguments.
%
%      FRMPRINCIPAL('Property','Value',...) creates a new FRMPRINCIPAL or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before frmPrincipal_OpeningFunction gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to frmPrincipal_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Copyright 2002-2003 The MathWorks, Inc.

% Edit the above text to modify the response to help frmPrincipal

% Last Modified by GUIDE v2.5 07-Mar-2007 12:47:43

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @frmPrincipal_OpeningFcn, ...
                   'gui_OutputFcn',  @frmPrincipal_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before frmPrincipal is made visible.
function frmPrincipal_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to frmPrincipal (see VARARGIN)

% Choose default command line output for frmPrincipal
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes frmPrincipal wait for user response (see UIRESUME)
% uiwait(handles.frmPrincipal);


% --- Outputs from this function are returned to the command line.
function varargout = frmPrincipal_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes on button press in btnExaminar.
function btnExaminar_Callback(hObject, eventdata, handles)
% hObject    handle to btnExaminar (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
    global filename pathname;
	[filename,pathname] = uigetfile({'*.jpg','Imágenes de Placas'});
	if filename ~= 0        
        encerarTextos();
        subplot(2,1,2); imshow(strcat(pathname,filename));
        title('Imagen capturada');
    end

   
        

function txtNroPlaca_Callback(hObject, eventdata, handles)
% hObject    handle to txtNroPlaca (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of txtNroPlaca as text
%        str2double(get(hObject,'String')) returns contents of txtNroPlaca as a double


% --- Executes during object creation, after setting all properties.
function txtNroPlaca_CreateFcn(hObject, eventdata, handles)
% hObject    handle to txtNroPlaca (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc
    set(hObject,'BackgroundColor','white');
else
    set(hObject,'BackgroundColor',get(0,'defaultUicontrolBackgroundColor'));
end



function btnReconocer_Callback(hObject, eventdata, handles)
% hObject    handle to btnReconocer (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
    global filename pathname; 
    Seg = '0';
	if filename ~= 0
        try           
            set(gcf,'Pointer','watch');
            h=gcf;
            placa=myOCR(pathname, filename);
            
            var=findobj(gcbf, 'Tag','txtNroPlaca');  % activa el control
            set(var,'String',placa);    % asigna el valor a la propiedad      

            set(h,'Pointer','arrow');
            figure(findobj('Tag','frmPrincipal')); % deja activa el figure
        catch
           set(h,'Pointer','arrow');
           msgbox('No se pudo reconocer la Placa','Procesando...', 'warn');
        end
    end
   

      
 function encerarTextos()
         var=findobj(gcbf, 'Tag','txtNroPlaca');  % activa el control
         set(var,'String','');    % asigna el valor a la propiedad        



% --- Executes on button press in btnCerrarVentanas.
function btnCerrarVentanas_Callback(hObject, eventdata, handles)
% hObject    handle to btnCerrarVentanas (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
   close all;



% --- Executes during object creation, after setting all properties.
function frmPrincipal_CreateFcn(hObject, eventdata, handles)
% hObject    handle to frmPrincipal (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called



