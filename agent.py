# Variable: guarda la pregunta del usuario
pregunta = input("¿Qué quieres saber? ")

# Función: procesa la pregunta
def responder(pregunta):
    if "película" in pregunta:
        return "Te recomiendo una película popular."
    else:
        return "No entiendo la pregunta."

# Acción: mostrar respuesta
respuesta = responder(pregunta)
print(respuesta)
