# Plantilla universal de docencia con Quarto

Infraestructura reutilizable mantenida por **Elmer Quispe-Salazar** para clases, talleres, cursos cortos, seminarios y cursos semestrales.

Este repositorio es la **plantilla fuente**. Los repositorios creados a partir de ella deben contener la actividad docente real y usar el topic de GitHub `type-training`. Este repositorio plantilla se mantiene como `type-template`.

## Objetivos de diseño

La plantilla sigue cinco principios:

1. **Estructura centrada en el aprendizaje**: cada módulo parte de una pregunta, objetivos de aprendizaje, prerrequisitos y tiempo estimado.
2. **Modularidad por tema**: notas, diapositivas, prácticas, ejercicios y notas del instructor de un mismo tema se mantienen juntos.
3. **Computación reproducible**: R, Python, Julia, C++, notebooks, bibliografía, código y pequeños datos docentes pueden convivir en un solo proyecto Quarto.
4. **Múltiples modalidades**: la misma estructura sirve para una clase única, un taller, un curso corto o un curso semestral.
5. **Integración académica**: los metadatos del repositorio pueden alimentar `qselmer.github.io/teaching/` y el perfil académico de GitHub.

## Estructura del repositorio

```text
.
├── template.yml                 # metadatos de esta plantilla
├── repo.yml                     # metadatos base del repositorio docente generado
├── course.yml                   # metadatos de la actividad docente
├── _quarto.yml                  # configuración del sitio Quarto
├── index.qmd                    # portada pública
├── syllabus.qmd                 # alcance, políticas y resultados esperados
├── schedule.qmd                 # cronograma o secuencia
├── setup.qmd                    # instalación y prerrequisitos
│
├── modules/
│   ├── index.qmd
│   └── 01-topic/
│       ├── module.yml           # metadatos estructurados del módulo
│       ├── index.qmd            # notas de clase o lección
│       ├── slides.qmd           # diapositivas reveal.js
│       ├── lab.qmd              # práctica guiada
│       ├── exercise.qmd         # ejercicio formativo
│       └── instructor-notes.md  # tiempos, errores frecuentes y notas docentes
│
├── assignments/                 # tareas o evaluaciones opcionales
├── project/                     # proyecto aplicado o capstone opcional
├── resources/                   # lecturas, enlaces y material de apoyo
├── data/                        # solo datos docentes pequeños
├── code/                        # scripts y funciones reutilizables
├── environment/                 # reproducibilidad, dependencias y lockfiles
├── assets/                      # CSS e imágenes
├── docs/                        # documentación de la plantilla
├── scripts/                     # utilidades de validación
├── references.bib
├── CITATION.cff
├── CONTRIBUTING.md
└── .github/workflows/publish.yml
```

## Estándar de autoría

Usa **Quarto `.qmd` como formato fuente canónico**. Conserva `.Rmd` solo durante la migración de material antiguo. Cada módulo debe ser suficientemente autocontenido para poder reutilizarse, reordenarse o adaptarse a otro curso sin reorganizar todo el repositorio.

## Crear un nuevo repositorio docente

1. Selecciona **Use this template → Create a new repository**.
2. Usa un nombre corto y descriptivo, por ejemplo `git-github-teaching`, `stock-assessment-teaching` o `spatial-models-workshop`.
3. Reemplaza los placeholders de `repo.yml`, `course.yml`, `_quarto.yml`, `CITATION.cff` y los archivos `.qmd`.
4. Añade exactamente un topic de tipo: `type-training`.
5. Añade `site-teaching` cuando la actividad deba aparecer en tu web académica.
6. Añade topics temáticos como `stock-assessment`, `mse`, `r`, `python`, `spatiotemporal-models` o `fisheries` según corresponda.
7. En el repositorio docente real, abre **Settings → Pages → Build and deployment → Source = GitHub Actions**.
8. Haz `push` a `main`; la validación y publicación se ejecutarán automáticamente.

Consulta [`docs/USING_TEMPLATE.md`](docs/USING_TEMPLATE.md) para el flujo completo.

## Comportamiento de la plantilla

Este repositorio plantilla se **valida y renderiza** en cada `push`, pero **no se publica en GitHub Pages**. Un repositorio docente creado a partir de esta plantilla sí se publicará cuando GitHub Pages esté habilitado en ese repositorio.

## Integración

El flujo esperado es:

```text
repositorio docente
      │
      ├── sitio del curso en GitHub Pages
      ├── entrada en qselmer.github.io/teaching/
      └── clasificación en el perfil académico de GitHub
```

Consulta [`docs/INTEGRATION.md`](docs/INTEGRATION.md).
