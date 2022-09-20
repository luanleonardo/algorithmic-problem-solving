from heapq import heapify, heappop, heappush
from sys import stdin, stdout

if __name__ == "__main__":
    num_integers = int(stdin.readline().strip())
    low_heap = []
    heapify(low_heap)
    high_heap = []
    heapify(high_heap)

    for i in range(1, num_integers + 1):
        x_i = int(stdin.readline().strip())
        l_i = -low_heap[0] if low_heap else float("-inf")
        h_i = high_heap[0] if high_heap else float("-inf")
        is_even_round = i % 2 == 0

        if x_i > h_i:
            heappush(high_heap, x_i)
            if is_even_round and len(low_heap) < len(high_heap):
                x = heappop(high_heap)
                heappush(low_heap, -x)
        else:
            heappush(low_heap, -x_i)
            if is_even_round and len(low_heap) > len(high_heap):
                x = -heappop(low_heap)
                heappush(high_heap, x)

        if is_even_round:
            m_i = (-low_heap[0] + high_heap[0]) / 2
        else:
            m_i = (
                -low_heap[0] if (i + 1) // 2 <= len(low_heap) else high_heap[0]
            ) / 1.0

        stdout.write(f"{m_i}\n")
