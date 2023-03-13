def modifier_mot(mot):
    lettres = list(mot)
    n = len(lettres)

    # Trouver la première lettre qui peut être échangée avec la suivante
    for i in range(n-2, -1, -1):
        if lettres[i] < lettres[i+1]:
            break
    else:
        return None  # le mot est déjà le plus grand possible

    # Trouver la lettre la plus petite à droite du pivot qui est plus grande que le pivot
    for j in range(n-1, i, -1):
        if lettres[j] > lettres[i]:
            break

    # Échanger les lettres
    lettres[i], lettres[j] = lettres[j], lettres[i]

    # Inverser la partie droite du mot
    lettres[i+1:] = reversed(lettres[i+1:])

    # Reconstruire le mot
    nouveau_mot = ''.join(lettres)
    return nouveau_mot

# Demander le mot à l'utilisateur
mot = input("Entrez un mot sans espace ni caractère spécial : ").lower()

# Modifier le mot
nouveau_mot = modifier_mot(mot)

if nouveau_mot is None:
    print("Le mot", mot, "est déjà le plus grand possible.")
else:
    print("Le mot suivant dans l'ordre alphabétique est :", nouveau_mot)