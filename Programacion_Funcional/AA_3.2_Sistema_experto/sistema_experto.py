
"""
Sistema Experto de Orientación Vocacional
    Hugo Sanchez  & Angel Jesus
==========================================
Puente Python-Prolog para recomendación de carreras universitarias.

Características funcionales aplicadas:
  - map()   : transformar respuestas del cuestionario a etiquetas
  - filter(): filtrar carreras por umbral de puntuación
  - Inmutabilidad: NamedTuple, frozenset, tuplas constantes

Requiere SWI-Prolog (swipl) instalado para el motor Prolog.
Si no está disponible, usa el motor de inferencia Python integrado.
"""

from __future__ import annotations

import os
import sys
import subprocess
import tempfile
import re
from typing import FrozenSet, Tuple, Sequence
from collections import namedtuple
from functools import reduce

# ═══════════════════════════════════════════════════════════════════════════════
#  ESTRUCTURAS INMUTABLES
# ═══════════════════════════════════════════════════════════════════════════════

PerfilUsuario = namedtuple('PerfilUsuario', ['nombre', 'habilidades', 'intereses', 'rasgos'])

ResultadoCarrera = namedtuple(
    'ResultadoCarrera',
    ['carrera_id', 'nombre', 'puntuacion', 'pts_habilidades', 'pts_intereses', 'pts_rasgos']
)

# ═══════════════════════════════════════════════════════════════════════════════
#  BASE DE CONOCIMIENTO PYTHON (espejo de base_conocimiento.pl)
# ═══════════════════════════════════════════════════════════════════════════════

CARRERAS: Tuple[Tuple[str, str], ...] = (
    ('sistemas_computacionales', 'Ing. en Sistemas Computacionales'),
    ('ciencia_de_datos',         'Ciencia de Datos'),
    ('administracion',           'Administración'),
    ('industrial',               'Ingeniería Industrial'),
    ('alimentarias',             'Ing. en Industrias Alimentarias'),
    ('desarrollo_comunitario',   'Lic. en Desarrollo Comunitario'),
    ('gestion_empresarial',      'Gestión Empresarial'),
)

HABILIDADES_POR_CARRERA: Tuple[Tuple[str, FrozenSet[str]], ...] = (
    ('sistemas_computacionales', frozenset({
        'programacion', 'logica_matematica', 'matematicas',
        'resolucion_problemas', 'pensamiento_abstracto',
    })),
    ('ciencia_de_datos', frozenset({
        'estadistica', 'matematicas', 'programacion',
        'analisis_datos', 'pensamiento_critico',
    })),
    ('administracion', frozenset({
        'liderazgo', 'comunicacion', 'organizacion',
        'toma_decisiones', 'trabajo_equipo',
    })),
    ('industrial', frozenset({
        'matematicas', 'optimizacion', 'fisica',
        'logistica', 'resolucion_problemas',
    })),
    ('alimentarias', frozenset({
        'quimica', 'biologia', 'ciencias_naturales',
        'investigacion', 'laboratorio',
    })),
    ('desarrollo_comunitario', frozenset({
        'empatia', 'comunicacion', 'liderazgo_social',
        'trabajo_equipo', 'pensamiento_critico',
    })),
    ('gestion_empresarial', frozenset({
        'finanzas', 'liderazgo', 'comunicacion',
        'planeacion', 'toma_decisiones',
    })),
)

INTERESES_POR_CARRERA: Tuple[Tuple[str, FrozenSet[str]], ...] = (
    ('sistemas_computacionales', frozenset({
        'tecnologia', 'videojuegos_software', 'redes_sistemas', 'automatizacion',
    })),
    ('ciencia_de_datos', frozenset({
        'investigacion', 'tecnologia', 'estadistica_aplicada', 'inteligencia_artificial',
    })),
    ('administracion', frozenset({
        'negocios', 'emprendimiento', 'recursos_humanos', 'gestion_organizacional',
    })),
    ('industrial', frozenset({
        'manufactura', 'procesos_productivos', 'ingenieria', 'calidad',
    })),
    ('alimentarias', frozenset({
        'salud', 'nutricion', 'ciencia_alimentos', 'medio_ambiente',
    })),
    ('desarrollo_comunitario', frozenset({
        'servicio_social', 'cultura', 'politica_social', 'derechos_humanos',
    })),
    ('gestion_empresarial', frozenset({
        'economia', 'negocios', 'finanzas_personales', 'emprendimiento',
    })),
)

RASGOS_POR_CARRERA: Tuple[Tuple[str, FrozenSet[str]], ...] = (
    ('sistemas_computacionales', frozenset({
        'analitico', 'detallista', 'persistente', 'independiente',
    })),
    ('ciencia_de_datos', frozenset({
        'curioso', 'analitico', 'meticuloso', 'independiente',
    })),
    ('administracion', frozenset({
        'lider', 'extrovertido', 'organizado', 'proactivo',
    })),
    ('industrial', frozenset({
        'sistematico', 'practico', 'analitico', 'orientado_resultados',
    })),
    ('alimentarias', frozenset({
        'curioso', 'meticuloso', 'practico', 'responsable',
    })),
    ('desarrollo_comunitario', frozenset({
        'empatico', 'comunicativo', 'comprometido', 'creativo',
    })),
    ('gestion_empresarial', frozenset({
        'lider', 'estrategico', 'proactivo', 'extrovertido',
    })),
)

# ═══════════════════════════════════════════════════════════════════════════════
#  MOTOR DE INFERENCIA PYTHON (funcional, inmutable)
# ═══════════════════════════════════════════════════════════════════════════════

PESOS: Tuple[int, int, int] = (3, 2, 1)   # habilidades, intereses, rasgos

def _dict_carrera(tabla: Tuple[Tuple[str, FrozenSet[str]], ...]) -> dict:
    """Convierte tabla inmutable a dict para lookup O(1). Función pura."""
    return dict(tabla)


def calcular_resultado(
    carrera_id: str,
    perfil: PerfilUsuario,
    *,
    nombres: dict,
    hab_map: dict,
    int_map: dict,
    ras_map: dict,
    pesos: Tuple[int, int, int] = PESOS,
) -> ResultadoCarrera:
    """Función pura: calcula la afinidad de una carrera para un perfil dado."""
    ph = len(perfil.habilidades & hab_map.get(carrera_id, frozenset()))
    pi = len(perfil.intereses    & int_map.get(carrera_id, frozenset()))
    pr = len(perfil.rasgos       & ras_map.get(carrera_id, frozenset()))
    total = ph * pesos[0] + pi * pesos[1] + pr * pesos[2]
    return ResultadoCarrera(
        carrera_id=carrera_id,
        nombre=nombres.get(carrera_id, carrera_id),
        puntuacion=total,
        pts_habilidades=ph,
        pts_intereses=pi,
        pts_rasgos=pr,
    )


def recomendar_python(
    perfil: PerfilUsuario,
    umbral: int = 0,
) -> Tuple[ResultadoCarrera, ...]:
    """
    Motor de inferencia Python puro.
    Aplica map + filter sobre las carreras; retorna tupla inmutable ordenada.
    """
    nombres  = dict(CARRERAS)
    hab_map  = _dict_carrera(HABILIDADES_POR_CARRERA)
    int_map  = _dict_carrera(INTERESES_POR_CARRERA)
    ras_map  = _dict_carrera(RASGOS_POR_CARRERA)

    ids = tuple(cid for cid, _ in CARRERAS)

    # map: calcular ResultadoCarrera para cada carrera
    resultados = tuple(map(
        lambda cid: calcular_resultado(
            cid, perfil,
            nombres=nombres, hab_map=hab_map,
            int_map=int_map, ras_map=ras_map,
        ),
        ids,
    ))

    # filter: solo carreras con puntuación mayor al umbral
    con_puntaje = tuple(filter(lambda r: r.puntuacion > umbral, resultados))

    # sorted (crea nueva tupla — inmutable)
    return tuple(sorted(con_puntaje, key=lambda r: r.puntuacion, reverse=True))


# ═══════════════════════════════════════════════════════════════════════════════
#  PUENTE PROLOG
# ═══════════════════════════════════════════════════════════════════════════════

def _swipl_disponible() -> bool:
    """Verifica si SWI-Prolog está instalado."""
    try:
        result = subprocess.run(
            ['swipl', '--version'],
            capture_output=True, timeout=5,
        )
        return result.returncode == 0
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False


def _lista_prolog(items: FrozenSet[str]) -> str:
    """Convierte un frozenset de Python a lista Prolog: [a,b,c]."""
    return '[' + ','.join(sorted(items)) + ']'


def recomendar_prolog(
    perfil: PerfilUsuario,
    ruta_pl: str,
) -> Tuple[ResultadoCarrera, ...] | None:
    """
    Ejecuta la consulta de recomendación en SWI-Prolog y parsea el resultado.
    Retorna None si falla; el caller hace fallback al motor Python.
    """
    h_str = _lista_prolog(perfil.habilidades)
    i_str = _lista_prolog(perfil.intereses)
    r_str = _lista_prolog(perfil.rasgos)

    goal = (
        f"use_module(library(lists)), "
        f"consult('{ruta_pl}'), "
        f"recomendar({h_str}, {i_str}, {r_str}, Rs), "
        f"maplist([P-C]>>(carrera(C,N), "
        f"  puntos_habilidades(C,{h_str},PH), "
        f"  puntos_intereses(C,{i_str},PI), "
        f"  puntos_rasgos(C,{r_str},PR), "
        f"  format('~w|~w|~w|~w|~w|~w~n',[C,N,P,PH,PI,PR])), Rs), halt."
    )

    try:
        proc = subprocess.run(
            ['swipl', '-g', goal, '-t', 'halt'],
            capture_output=True, text=True, timeout=15,
        )
        lineas = [l.strip() for l in proc.stdout.splitlines() if '|' in l]
        if not lineas:
            return None

        def parsear_linea(linea: str) -> ResultadoCarrera:
            cid, nombre, total, ph, pi, pr = linea.split('|')
            return ResultadoCarrera(
                carrera_id=cid,
                nombre=nombre,
                puntuacion=int(total),
                pts_habilidades=int(ph),
                pts_intereses=int(pi),
                pts_rasgos=int(pr),
            )

        return tuple(map(parsear_linea, lineas))

    except Exception:
        return None


# ═══════════════════════════════════════════════════════════════════════════════
#  CUESTIONARIO INTERACTIVO
# ═══════════════════════════════════════════════════════════════════════════════

PREGUNTAS: Tuple = (

    # ── HABILIDADES ──────────────────────────────────────────────────────────
    (
        "1. ¿Cómo calificarías tu habilidad en matemáticas y cálculo?",
        (
            ("Excelente — los números son mi fuerte",
             ('matematicas', 'logica_matematica', 'estadistica'), (), ('analitico',)),
            ("Buena — me desenvuelvo bien",
             ('matematicas',), (), ()),
            ("Regular — lo básico está bien",
             (), (), ()),
            ("No es mi fuerte",
             (), (), ()),
        ),
    ),
    (
        "2. ¿Tienes habilidad o experiencia en programación?",
        (
            ("Sí, programo con facilidad",
             ('programacion', 'pensamiento_abstracto'), ('tecnologia',), ('analitico',)),
            ("He programado algo y me resulta fácil",
             ('programacion',), ('tecnologia',), ()),
            ("Lo he intentado pero me cuesta trabajo",
             (), (), ()),
            ("No tengo experiencia",
             (), (), ()),
        ),
    ),
    (
        "3. ¿Qué tan bueno/a eres liderando grupos o tomando decisiones?",
        (
            ("Muy bueno/a — me encanta organizar y dirigir",
             ('liderazgo', 'toma_decisiones', 'organizacion'), (), ('lider', 'proactivo')),
            ("Bueno/a — puedo hacerlo cuando es necesario",
             ('liderazgo', 'toma_decisiones'), (), ('organizado',)),
            ("Prefiero seguir instrucciones",
             (), (), ('independiente',)),
            ("No me siento cómodo/a liderando",
             (), (), ()),
        ),
    ),
    (
        "4. ¿Cómo te desempeñas en ciencias naturales (biología, química)?",
        (
            ("Excelente — me apasionan",
             ('biologia', 'quimica', 'ciencias_naturales', 'laboratorio'), ('salud', 'ciencia_alimentos'), ('curioso',)),
            ("Bien — tengo buenas bases",
             ('biologia', 'quimica'), ('salud',), ()),
            ("Regular",
             (), (), ()),
            ("No es lo mío",
             (), (), ()),
        ),
    ),
    (
        "5. ¿Tienes facilidad para comunicarte y trabajar en equipo?",
        (
            ("Sí, soy muy comunicativo/a y colaborativo/a",
             ('comunicacion', 'trabajo_equipo', 'empatia'), (), ('comunicativo', 'extrovertido')),
            ("Soy buen/a comunicador/a",
             ('comunicacion', 'trabajo_equipo'), (), ()),
            ("Prefiero trabajar de forma más independiente",
             (), (), ('independiente',)),
            ("Me cuesta relacionarme con otros",
             (), (), ()),
        ),
    ),
    (
        "6. ¿Tienes habilidad para analizar datos, hacer estadísticas o investigar?",
        (
            ("Sí — me gusta investigar y analizar",
             ('estadistica', 'analisis_datos', 'investigacion', 'pensamiento_critico'),
             ('investigacion', 'estadistica_aplicada'), ('meticuloso', 'curioso')),
            ("Tengo bases y me interesa desarrollarlo",
             ('estadistica', 'analisis_datos'), ('investigacion',), ()),
            ("Poco",
             (), (), ()),
            ("No, no es algo que se me dé bien",
             (), (), ()),
        ),
    ),
    (
        "7. ¿Qué tan hábil eres para planear, optimizar procesos o resolver problemas prácticos?",
        (
            ("Muy hábil — me encanta mejorar procesos",
             ('optimizacion', 'planeacion', 'logistica', 'resolucion_problemas'),
             ('procesos_productivos', 'calidad'), ('sistematico', 'orientado_resultados')),
            ("Hábil — puedo hacerlo bien",
             ('optimizacion', 'resolucion_problemas'), (), ('practico',)),
            ("Regular",
             (), (), ()),
            ("No es mi fortaleza",
             (), (), ()),
        ),
    ),
    (
        "8. ¿Tienes habilidades en finanzas, contabilidad o gestión de recursos?",
        (
            ("Sí, entiendo bien el manejo de dinero y presupuestos",
             ('finanzas', 'planeacion', 'toma_decisiones'),
             ('economia', 'finanzas_personales'), ('estrategico',)),
            ("Tengo nociones básicas",
             ('finanzas',), ('economia',), ()),
            ("Muy poco",
             (), (), ()),
            ("No tengo conocimientos financieros",
             (), (), ()),
        ),
    ),

    # ── INTERESES ────────────────────────────────────────────────────────────
    (
        "9. ¿Qué área te apasiona más?",
        (
            ("Tecnología, software o inteligencia artificial",
             (), ('tecnologia', 'videojuegos_software', 'inteligencia_artificial', 'automatizacion'), ()),
            ("Negocios, emprendimiento o economía",
             (), ('negocios', 'emprendimiento', 'economia', 'gestion_organizacional'), ()),
            ("Salud, alimentación o medio ambiente",
             (), ('salud', 'nutricion', 'ciencia_alimentos', 'medio_ambiente'), ()),
            ("Sociedad, cultura o derechos humanos",
             (), ('servicio_social', 'cultura', 'politica_social', 'derechos_humanos'), ()),
        ),
    ),
    (
        "10. ¿Qué actividad disfrutas más en tu tiempo libre?",
        (
            ("Programar, armar o reparar cosas electrónicas/computadoras",
             ('programacion',), ('tecnologia', 'redes_sistemas'), ('analitico', 'detallista')),
            ("Leer sobre economía, negocios o gestión",
             (), ('negocios', 'recursos_humanos', 'gestion_organizacional'), ('estrategico',)),
            ("Cocinar, estudiar nutrición o hacer experimentos",
             ('laboratorio',), ('nutricion', 'ciencia_alimentos'), ('practico', 'curioso')),
            ("Voluntariado, trabajo social o activismo",
             ('empatia', 'liderazgo_social'), ('servicio_social', 'derechos_humanos'), ('empatico', 'comprometido')),
        ),
    ),
    (
        "11. ¿Cuál de estos temas te resulta más interesante?",
        (
            ("Análisis de datos, estadística o machine learning",
             ('estadistica', 'analisis_datos'), ('estadistica_aplicada', 'inteligencia_artificial'), ('curioso', 'meticuloso')),
            ("Gestión de empresas o administración pública",
             ('organizacion', 'planeacion'), ('recursos_humanos', 'gestion_organizacional'), ('organizado',)),
            ("Producción industrial o control de calidad",
             ('optimizacion', 'fisica'), ('manufactura', 'calidad', 'ingenieria'), ('sistematico',)),
            ("Desarrollo sostenible o bienestar comunitario",
             ('empatia',), ('politica_social', 'cultura', 'medio_ambiente'), ('comprometido', 'creativo')),
        ),
    ),

    # ── RASGOS DE PERSONALIDAD ───────────────────────────────────────────────
    (
        "12. ¿Cómo te describirías mejor?",
        (
            ("Analítico/a e independiente — prefiero resolver problemas solo/a",
             (), (), ('analitico', 'independiente', 'detallista')),
            ("Líder y extrovertido/a — me energiza trabajar con personas",
             (), (), ('lider', 'extrovertido', 'proactivo')),
            ("Empático/a y creativo/a — me importa el impacto social",
             (), (), ('empatico', 'comunicativo', 'comprometido', 'creativo')),
            ("Práctico/a y meticuloso/a — me gustan los resultados concretos",
             (), (), ('practico', 'meticuloso', 'responsable', 'orientado_resultados')),
        ),
    ),
    (
        "13. Ante un problema nuevo, ¿qué haces primero?",
        (
            ("Investigo, recopilo datos y busco patrones",
             ('pensamiento_critico', 'analisis_datos'), ('investigacion',), ('curioso', 'analitico')),
            ("Organizo un plan de acción y delego tareas",
             ('organizacion', 'toma_decisiones'), (), ('organizado', 'estrategico', 'lider')),
            ("Busco cómo afecta a las personas involucradas",
             ('empatia',), ('servicio_social',), ('empatico', 'comunicativo')),
            ("Encuentro la forma más eficiente de resolverlo",
             ('optimizacion', 'resolucion_problemas'), (), ('sistematico', 'orientado_resultados', 'persistente')),
        ),
    ),
    (
        "14. ¿Cómo prefieres trabajar?",
        (
            ("Solo/a, con autonomía y concentración",
             (), (), ('independiente', 'persistente', 'detallista')),
            ("En equipo, coordinando personas y recursos",
             ('trabajo_equipo', 'comunicacion'), (), ('extrovertido', 'proactivo', 'lider')),
            ("En campo, directamente con comunidades o en planta",
             ('trabajo_equipo',), ('servicio_social', 'manufactura'), ('practico', 'comprometido')),
            ("En laboratorio o entornos controlados",
             ('laboratorio', 'investigacion'), ('ciencia_alimentos',), ('meticuloso', 'responsable')),
        ),
    ),
)


def leer_opcion(prompt: str, n_opciones: int) -> int:
    """Lee una opción válida del usuario (1..n). Función pura de I/O."""
    while True:
        try:
            val = int(input(prompt).strip())
            if 1 <= val <= n_opciones:
                return val - 1
            print(f"  Por favor ingresa un número entre 1 y {n_opciones}.")
        except (ValueError, KeyboardInterrupt):
            print("\n  Entrada inválida. Intenta de nuevo.")


def acumular_tags(
    respuestas: Tuple[Tuple[Tuple[str, ...], Tuple[str, ...], Tuple[str, ...]], ...],
) -> Tuple[FrozenSet[str], FrozenSet[str], FrozenSet[str]]:
    """
    Reduce las respuestas del cuestionario (inmutables) a tres frozensets.
    Usa reduce() para acumular tags por categoría — función pura.
    """
    def _combinar(acc, resp):
        h_acc, i_acc, r_acc = acc
        h_new, i_new, r_new = resp
        return (
            h_acc | frozenset(h_new),
            i_acc | frozenset(i_new),
            r_acc | frozenset(r_new),
        )

    hab, inter, ras = reduce(_combinar, respuestas, (frozenset(), frozenset(), frozenset()))
    return frozenset(hab), frozenset(inter), frozenset(ras)


def ejecutar_cuestionario() -> PerfilUsuario:
    """Presenta el cuestionario interactivo y retorna un PerfilUsuario inmutable."""
    _sep()
    print("  🎓  SISTEMA EXPERTO DE ORIENTACIÓN VOCACIONAL")
    print("           Hugo Sanchez leyva & Angel Jesús Balam Dzidz")
    _sep()
    print("  Responde las siguientes preguntas seleccionando la opción que")
    print("  mejor te describa. No hay respuestas correctas o incorrectas.\n")

    nombre = input("  ¿Cuál es tu nombre? → ").strip() or "Estudiante"
    print()

    respuestas_acumuladas = []

    for pregunta, opciones in PREGUNTAS:
        print(f"  {pregunta}")
        for idx, (texto, *_) in enumerate(opciones, 1):
            print(f"    {idx}. {texto}")
        seleccion = leer_opcion("  Tu elección: ", len(opciones))
        _, h_tags, i_tags, r_tags = opciones[seleccion]
        respuestas_acumuladas.append((h_tags, i_tags, r_tags))
        print()

    habs, inters, rasgos = acumular_tags(tuple(respuestas_acumuladas))
    return PerfilUsuario(nombre=nombre, habilidades=habs, intereses=inters, rasgos=rasgos)


# ═══════════════════════════════════════════════════════════════════════════════
#  PRESENTACIÓN DE RESULTADOS
# ═══════════════════════════════════════════════════════════════════════════════

BARRA = "█"

def barra_progreso(pts: int, maximo: int, ancho: int = 20) -> str:
    """Genera una barra de texto proporcional a la puntuación."""
    llenos = int((pts / maximo) * ancho) if maximo > 0 else 0
    return BARRA * llenos + "░" * (ancho - llenos)


def _sep(char: str = "─", n: int = 60) -> None:
    print("  " + char * n)


def mostrar_resultados(
    perfil: PerfilUsuario,
    resultados: Tuple[ResultadoCarrera, ...],
    motor: str,
) -> None:
    """Imprime los resultados del sistema experto en la terminal."""
    _sep("═")
    print(f"\n  Resultados para: {perfil.nombre}   [motor: {motor}]\n")
    _sep()

    if not resultados:
        print("  No se encontraron carreras con afinidad. Intenta responder más preguntas.")
        return

    maximo = resultados[0].puntuacion

    for rank, r in enumerate(resultados, 1):
        porcentaje = int((r.puntuacion / maximo) * 100) if maximo > 0 else 0
        barra = barra_progreso(r.puntuacion, maximo)
        print(f"  #{rank}  {r.nombre}")
        print(f"      {barra}  {r.puntuacion} pts ({porcentaje}%)")
        print(f"      Habilidades: {r.pts_habilidades}  |  "
              f"Intereses: {r.pts_intereses}  |  Rasgos: {r.pts_rasgos}")
        print()

    _sep()
    print(f"\n  🥇 Carrera más recomendada: {resultados[0].nombre}")
    print(f"     Puntuación total: {resultados[0].puntuacion} puntos\n")

    print("  Tu perfil detectado:")
    print(f"    Habilidades : {', '.join(sorted(perfil.habilidades)) or 'ninguna'}")
    print(f"    Intereses   : {', '.join(sorted(perfil.intereses)) or 'ninguno'}")
    print(f"    Rasgos      : {', '.join(sorted(perfil.rasgos)) or 'ninguno'}")
    print()
    _sep("═")


# ═══════════════════════════════════════════════════════════════════════════════
#  PUNTO DE ENTRADA
# ═══════════════════════════════════════════════════════════════════════════════

def main() -> None:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    ruta_pl = os.path.join(script_dir, 'base_conocimiento.pl')

    perfil = ejecutar_cuestionario()

    if os.path.exists(ruta_pl) and _swipl_disponible():
        motor = "SWI-Prolog"
        print("  🔗 Conectando con motor Prolog...")
        resultados = recomendar_prolog(perfil, ruta_pl)
        if resultados is None:
            print("  ⚠️  Prolog no respondió correctamente. Usando motor Python.")
            motor = "Python (fallback)"
            resultados = recomendar_python(perfil)
    else:
        motor = "Python (integrado)"
        resultados = recomendar_python(perfil)

    mostrar_resultados(perfil, resultados, motor)


if __name__ == '__main__':
    main()
