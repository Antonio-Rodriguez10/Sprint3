
# Sprint 3 – Agentes 101 (Agente simple con API)

## 1) Propósito del agente
Este proyecto es un primer paso para crear un agente inteligente sencillo.  
El agente permite buscar películas en The Movie Database (TMDB) a partir de lo que escribe el usuario y devuelve resultados con título, año y rating.

La idea es practicar un flujo básico de interacción (pregunta → procesamiento → respuesta), sin necesidad de código complejo.

## 2) Herramienta asistida por IA utilizada
Para generar y ajustar el ejemplo he usado **GitHub Copilot o Cursor** (según disponibilidad).  
La IA ayuda a:
- proponer la estructura del script,
- completar funciones,
- corregir errores típicos,
- mejorar el formato de la salida.

## 3) Flujo lógico de la interacción
1. El usuario escribe un título de película.
2. El agente valida la entrada (por ejemplo, que no esté vacía).
3. El agente consulta TMDB (API externa).
4. El agente filtra y formatea los 5 resultados principales.
5. El agente responde en texto con las recomendaciones.

## 4) Ejemplo de interacción (resultado)
Tú: matrix  
Agente:
1. The Matrix (1999) — rating: 8.2/10
2. The Matrix Reloaded (2003) — rating: 7.0/10
...

## 5) Fundamentos de programación que aparecen (explicado simple)
- **Variables**: son “cajas” donde guardo datos, por ejemplo el texto que escribe el usuario o la lista de resultados.
- **Condicionales (if/else)**: sirven para tomar decisiones. Ej: si el usuario escribe “salir”, el programa termina.
- **Bucles (while)**: permiten repetir la interacción para que el usuario pueda hacer varias búsquedas seguidas.
- **Funciones**: son “recetas reutilizables”. Ej: una función para buscar en la API y otra para formatear los resultados.

## 6) Cómo ejecutar el proyecto
1. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
