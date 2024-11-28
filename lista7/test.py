def is_identical(G, H):
    # Zakładamy, że G i H mają tę samą liczbę wierzchołków
    n = len(G)  # Liczba wierzchołków
    visited = [False] * n  # Tablica śledząca odwiedzone wierzchołki

    for vertex in range(n):  # Iterujemy po wszystkich wierzchołkach
        nodes_diff = 0  # Licznik różnicy krawędzi
        
        # Iterujemy po sąsiadach wierzchołka w grafie G
        for neighbour in G[vertex]:
            visited[neighbour] = True
            nodes_diff += 1

        # Iterujemy po sąsiadach wierzchołka w grafie H
        for neighbour in H[vertex]:
            if visited[neighbour] == False:
                return False  # Sąsiad z H nie istnieje w G
            visited[neighbour] = False
            nodes_diff -= 1

        # Jeśli liczba krawędzi nie jest zgodna, grafy różnią się
        if nodes_diff != 0:
            return False

    return True  # Grafy są identyczne

G = [[], [3, 2], [1, 3], [1, 2]]
H = [[], [3, 2], [3, 1], [2, 1]]
print(is_identical(G, H))