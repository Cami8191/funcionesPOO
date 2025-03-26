import random 

# Realizar función probabilidad
def probabilidad(num_lanzamientos):
    # Simular los lanzamientos de la moneda
    resultados = [random.choice([0, 1]) for _ in range(num_lanzamientos)]
    
    # Calcular la probabilidad de obtener caras (representadas por 1)
    prob = resultados.count(1) / num_lanzamientos
    return prob

# Ejemplo de uso (declaración de objetos)
num_lanzamientos = 10

prob = probabilidad(num_lanzamientos)
print(f"La probabilidad de obtener caras en {num_lanzamientos} lanzamientos es {prob:.4f}")s es {prob:.4f}")} es {prob: .4f} ")