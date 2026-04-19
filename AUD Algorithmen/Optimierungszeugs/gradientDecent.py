def g(x):
    return sum(a ** 3 + a ** 2 for a in x)  # Wendet g auf jedes Element an und summiert


def gradient_descent(x, n, delta_x, accuracy):
    x = list(x)  # Konvertiere x in eine Liste
    grad = [0] * len(x)  # Initialisiere grad als Liste

    while g(x) > accuracy:
        for i in range(len(x)):  # Iteriere über alle Komponenten von x
            d_x = [0] * len(x)  # Erzeuge einen Nullvektor als Liste
            d_x[i] = delta_x  # Setze die i-te Komponente auf delta_x

            # Berechne die zentrale Differenz
            grad[i] = (g([x[j] + d_x[j] for j in range(len(x))]) - g([x[j] - d_x[j] for j in range(len(x))])) / (
                        2 * delta_x)


        # Aktualisiere x mit der Lernrate n
        x = [x[j] - n * grad[j] for j in range(len(x))]
    print(grad)
    print(x)
    return tuple(x)  # Konvertiere x zurück in ein Tupel für die Ausgabe


# Beispielaufruf:
result = gradient_descent((4, 1, 3), 0.01, 0.01, 0.00000001)
print(g(result))


print(result)
