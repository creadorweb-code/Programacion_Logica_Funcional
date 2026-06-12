% =============================================================================
%  BASE DE CONOCIMIENTO - SISTEMA EXPERTO DE ORIENTACION VOCACIONAL
%  Carreras: Sistemas Computacionales, Ciencia de Datos, Administracion,
%            Industrial, Alimentarias, Desarrollo Comunitario, Gestion Empresarial
% =============================================================================

:- set_prolog_flag(encoding, utf8).

% ─────────────────────────────────────────────────────────────────────────────
%  CATALOGO DE CARRERAS
% ─────────────────────────────────────────────────────────────────────────────

carrera(sistemas_computacionales,  'Ingenieria en Sistemas Computacionales').
carrera(ciencia_de_datos,          'Ciencia de Datos').
carrera(administracion,            'Administracion').
carrera(industrial,                'Ingenieria Industrial').
carrera(alimentarias,              'Ingenieria en Industrias Alimentarias').
carrera(desarrollo_comunitario,    'Licenciatura en Desarrollo Comunitario').
carrera(gestion_empresarial,       'Gestion Empresarial').

% ─────────────────────────────────────────────────────────────────────────────
%  HABILIDADES REQUERIDAS POR CARRERA
% ─────────────────────────────────────────────────────────────────────────────

habilidad_requerida(sistemas_computacionales, programacion).
habilidad_requerida(sistemas_computacionales, logica_matematica).
habilidad_requerida(sistemas_computacionales, matematicas).
habilidad_requerida(sistemas_computacionales, resolucion_problemas).
habilidad_requerida(sistemas_computacionales, pensamiento_abstracto).

habilidad_requerida(ciencia_de_datos, estadistica).
habilidad_requerida(ciencia_de_datos, matematicas).
habilidad_requerida(ciencia_de_datos, programacion).
habilidad_requerida(ciencia_de_datos, analisis_datos).
habilidad_requerida(ciencia_de_datos, pensamiento_critico).

habilidad_requerida(administracion, liderazgo).
habilidad_requerida(administracion, comunicacion).
habilidad_requerida(administracion, organizacion).
habilidad_requerida(administracion, toma_decisiones).
habilidad_requerida(administracion, trabajo_equipo).

habilidad_requerida(industrial, matematicas).
habilidad_requerida(industrial, optimizacion).
habilidad_requerida(industrial, fisica).
habilidad_requerida(industrial, logistica).
habilidad_requerida(industrial, resolucion_problemas).

habilidad_requerida(alimentarias, quimica).
habilidad_requerida(alimentarias, biologia).
habilidad_requerida(alimentarias, ciencias_naturales).
habilidad_requerida(alimentarias, investigacion).
habilidad_requerida(alimentarias, laboratorio).

habilidad_requerida(desarrollo_comunitario, empatia).
habilidad_requerida(desarrollo_comunitario, comunicacion).
habilidad_requerida(desarrollo_comunitario, liderazgo_social).
habilidad_requerida(desarrollo_comunitario, trabajo_equipo).
habilidad_requerida(desarrollo_comunitario, pensamiento_critico).

habilidad_requerida(gestion_empresarial, finanzas).
habilidad_requerida(gestion_empresarial, liderazgo).
habilidad_requerida(gestion_empresarial, comunicacion).
habilidad_requerida(gestion_empresarial, planeacion).
habilidad_requerida(gestion_empresarial, toma_decisiones).

% ─────────────────────────────────────────────────────────────────────────────
%  INTERESES ASOCIADOS A CADA CARRERA
% ─────────────────────────────────────────────────────────────────────────────

interes_carrera(sistemas_computacionales, tecnologia).
interes_carrera(sistemas_computacionales, videojuegos_software).
interes_carrera(sistemas_computacionales, redes_sistemas).
interes_carrera(sistemas_computacionales, automatizacion).

interes_carrera(ciencia_de_datos, investigacion).
interes_carrera(ciencia_de_datos, tecnologia).
interes_carrera(ciencia_de_datos, estadistica_aplicada).
interes_carrera(ciencia_de_datos, inteligencia_artificial).

interes_carrera(administracion, negocios).
interes_carrera(administracion, emprendimiento).
interes_carrera(administracion, recursos_humanos).
interes_carrera(administracion, gestion_organizacional).

interes_carrera(industrial, manufactura).
interes_carrera(industrial, procesos_productivos).
interes_carrera(industrial, ingenieria).
interes_carrera(industrial, calidad).

interes_carrera(alimentarias, salud).
interes_carrera(alimentarias, nutricion).
interes_carrera(alimentarias, ciencia_alimentos).
interes_carrera(alimentarias, medio_ambiente).

interes_carrera(desarrollo_comunitario, servicio_social).
interes_carrera(desarrollo_comunitario, cultura).
interes_carrera(desarrollo_comunitario, politica_social).
interes_carrera(desarrollo_comunitario, derechos_humanos).

interes_carrera(gestion_empresarial, economia).
interes_carrera(gestion_empresarial, negocios).
interes_carrera(gestion_empresarial, finanzas_personales).
interes_carrera(gestion_empresarial, emprendimiento).

% ─────────────────────────────────────────────────────────────────────────────
%  RASGOS DE PERSONALIDAD POR CARRERA
% ─────────────────────────────────────────────────────────────────────────────

rasgo_carrera(sistemas_computacionales, analitico).
rasgo_carrera(sistemas_computacionales, detallista).
rasgo_carrera(sistemas_computacionales, persistente).
rasgo_carrera(sistemas_computacionales, independiente).

rasgo_carrera(ciencia_de_datos, curioso).
rasgo_carrera(ciencia_de_datos, analitico).
rasgo_carrera(ciencia_de_datos, meticuloso).
rasgo_carrera(ciencia_de_datos, independiente).

rasgo_carrera(administracion, lider).
rasgo_carrera(administracion, extrovertido).
rasgo_carrera(administracion, organizado).
rasgo_carrera(administracion, proactivo).

rasgo_carrera(industrial, sistematico).
rasgo_carrera(industrial, practico).
rasgo_carrera(industrial, analitico).
rasgo_carrera(industrial, orientado_resultados).

rasgo_carrera(alimentarias, curioso).
rasgo_carrera(alimentarias, meticuloso).
rasgo_carrera(alimentarias, practico).
rasgo_carrera(alimentarias, responsable).

rasgo_carrera(desarrollo_comunitario, empatico).
rasgo_carrera(desarrollo_comunitario, comunicativo).
rasgo_carrera(desarrollo_comunitario, comprometido).
rasgo_carrera(desarrollo_comunitario, creativo).

rasgo_carrera(gestion_empresarial, lider).
rasgo_carrera(gestion_empresarial, estrategico).
rasgo_carrera(gestion_empresarial, proactivo).
rasgo_carrera(gestion_empresarial, extrovertido).

% ─────────────────────────────────────────────────────────────────────────────
%  REGLAS DE INFERENCIA
% ─────────────────────────────────────────────────────────────────────────────

%% puntos_habilidades(+Carrera, +ListaHabilidades, -Puntos)
puntos_habilidades(Carrera, Habilidades, Puntos) :-
    findall(H, (member(H, Habilidades), habilidad_requerida(Carrera, H)), Matches),
    length(Matches, Puntos).

%% puntos_intereses(+Carrera, +ListaIntereses, -Puntos)
puntos_intereses(Carrera, Intereses, Puntos) :-
    findall(I, (member(I, Intereses), interes_carrera(Carrera, I)), Matches),
    length(Matches, Puntos).

%% puntos_rasgos(+Carrera, +ListaRasgos, -Puntos)
puntos_rasgos(Carrera, Rasgos, Puntos) :-
    findall(R, (member(R, Rasgos), rasgo_carrera(Carrera, R)), Matches),
    length(Matches, Puntos).

%% puntuacion_total(+Carrera, +Habilidades, +Intereses, +Rasgos, -Total)
%  Pesos: habilidades*3, intereses*2, rasgos*1
puntuacion_total(Carrera, Habilidades, Intereses, Rasgos, Total) :-
    puntos_habilidades(Carrera, Habilidades, PH),
    puntos_intereses(Carrera, Intereses, PI),
    puntos_rasgos(Carrera, Rasgos, PR),
    Total is (PH * 3) + (PI * 2) + (PR * 1).

%% afin(+Carrera, +Habilidades, +Intereses, +Rasgos)
%  Una carrera es afin si tiene al menos 1 punto
afin(Carrera, Habilidades, Intereses, Rasgos) :-
    puntuacion_total(Carrera, Habilidades, Intereses, Rasgos, Total),
    Total > 0.

%% todas_puntuaciones(+Habilidades, +Intereses, +Rasgos, -Pares)
%  Recolecta pares Puntuacion-Carrera para todas las carreras
todas_puntuaciones(Habilidades, Intereses, Rasgos, Pares) :-
    findall(
        Total-Carrera,
        (carrera(Carrera, _), puntuacion_total(Carrera, Habilidades, Intereses, Rasgos, Total)),
        Pares
    ).

%% recomendar(+Habilidades, +Intereses, +Rasgos, -Ordenadas)
%  Regla principal: lista [Puntos-Carrera] ordenada descendentemente
recomendar(Habilidades, Intereses, Rasgos, Ordenadas) :-
    todas_puntuaciones(Habilidades, Intereses, Rasgos, Pares),
    msort(Pares, Ascendente),
    reverse(Ascendente, Ordenadas).

%% detalle_carrera(+Carrera, +H, +I, +R, -Nombre, -Total, -PH, -PI, -PR)
detalle_carrera(Carrera, H, I, R, Nombre, Total, PH, PI, PR) :-
    carrera(Carrera, Nombre),
    puntos_habilidades(Carrera, H, PH),
    puntos_intereses(Carrera, I, PI),
    puntos_rasgos(Carrera, R, PR),
    Total is (PH * 3) + (PI * 2) + (PR * 1).
