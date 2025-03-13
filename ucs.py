# -*- coding: utf-8 -*-
"""UCS

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10GyAHF97O8uMjfA93saSLsTMcW4M6Kww
"""

import heapq

# Uniform Cost Search (UCS)
def uniform_cost_search(graph, cost, start, goal):
    # Priority Queue (heap)
    queue = []
    heapq.heappush(queue, (0, start, []))  # (biaya, simpul, jalur)

    # Set untuk menyimpan simpul yang sudah dikunjungi
    visited = set()

    while queue:
        biaya_sekarang, simpul, jalur = heapq.heappop(queue)

        if simpul in visited:
            continue

        visited.add(simpul)
        jalur = jalur + [simpul]

        # Jika sudah sampai di tujuan, kembalikan hasilnya
        if simpul == goal:
            return biaya_sekarang, jalur

        # Mengeksplorasi tetangga dari simpul saat ini
        for tetangga in graph.get(simpul, []):  # Gunakan .get() agar tidak error jika simpul tidak ada
            if tetangga not in visited:
                total_biaya = biaya_sekarang + cost.get((simpul, tetangga), float("inf"))
                heapq.heappush(queue, (total_biaya, tetangga, jalur))

    return float("inf"), []  # Jika tujuan tidak dapat dicapai

# Fungsi utama
if __name__ == '__main__':  # Perbaikan pada __name__ dan __main__
    # Graph dengan simpul berupa huruf
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['E', 'F'],
        'D': ['G'],
        'E': ['G'],
        'F': ['G'],
        'G': []
    }

    # Menetapkan biaya antar simpul
    cost = {
        ('A', 'B'): 4,
        ('A', 'C'): 3,
        ('B', 'D'): 5,
        ('B', 'E'): 6,
        ('C', 'E'): 2,
        ('C', 'F'): 4,
        ('D', 'G'): 3,
        ('E', 'G'): 2,
        ('F', 'G'): 5
    }

    # Menetapkan simpul tujuan
    tujuan = 'G'  # Sekarang sebagai string, bukan set

    # Menjalankan Uniform Cost Search dari simpul A ke simpul tujuan G
    biaya_minimum, jalur = uniform_cost_search(graph, cost, 'A', tujuan)

    # Output hasil pencarian UCS dalam bahasa Indonesia
    print("Biaya minimum dari simpul A ke simpul G adalah:", biaya_minimum)
    print("Jalur yang ditempuh:", " → ".join(jalur))