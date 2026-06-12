# Sistema Experto de Orientación Vocacional

Creado por **Hugo Sánchez Leyva** y **Ángel Jesús Balam Dzidz**.

Proyecto colaborativo que implementa un sistema experto para recomendar carreras universitarias de acuerdo con las habilidades, intereses y rasgos de personalidad del estudiante.

El sistema combina:

- Paradigma lógico (Prolog) como motor de inferencia.
- Paradigma funcional (Python) como interfaz y motor alternativo.

---

# Características

- Cuestionario interactivo de 14 preguntas.
- Recomendación de carreras basada en habilidades, intereses y rasgos de personalidad.
- Base de conocimiento en Prolog.
- Motor de inferencia implementado también en Python.
- Uso de map(), filter() y reduce().
- Estructuras inmutables: namedtuple, tuple y frozenset.

---

# Carreras consideradas

1. Ingeniería en Sistemas Computacionales.
2. Ciencia de Datos.
3. Administración.
4. Ingeniería Industrial.
5. Ingeniería en Industrias Alimentarias.
6. Licenciatura en Desarrollo Comunitario.
7. Gestión Empresarial.

---

# Archivos del proyecto

```text
Proyecto/
│
├── sistema_experto.py
├── base_conocimiento.pl
└── README.md
```

---

# Requisitos

## Python

Python 3.10 o superior.

Verificar:

```bash
python --version
```

## SWI-Prolog (opcional)

```bash
swipl --version
```

---

# Instrucciones de ejecución

1. Colocar los archivos `sistema_experto.py` y `base_conocimiento.pl` en la misma carpeta.
2. Abrir PowerShell, CMD o Git Bash.
3. Ir a la carpeta del proyecto.

```bash
cd ruta_del_proyecto
```

4. Ejecutar:

```bash
python sistema_experto.py
```

Si SWI-Prolog está instalado, se utilizará como motor de inferencia. En caso contrario, el sistema utilizará automáticamente el motor Python integrado.

---

# Programación funcional utilizada

- map()
- filter()
- reduce()
- namedtuple
- tuple
- frozenset

---

# Tecnologías utilizadas

- Python 3
- SWI-Prolog
- Programación funcional
- Sistemas expertos

---

# Autores

- Hugo Sánchez Leyva
- Ángel Jesús Balam Dzidz

Proyecto académico desarrollado con fines educativos.
