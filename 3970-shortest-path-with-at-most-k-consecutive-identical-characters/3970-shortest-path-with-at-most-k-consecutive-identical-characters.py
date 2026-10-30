import heapq

class Solution:
    def shortestPath(self, n, edges, labels, k):

        adj = [[] for _ in range(n)]

        # Build graph
        for u, v, w in edges:
            adj[u].append((v, w))

        dist = [[float("inf")] * (k + 1) for _ in range(n)]

        # (distance, node, remainingK)
        pq = [(0, 0, k)]

        dist[0][k] = 0

        while pq:

            d, u, rem = heapq.heappop(pq)

            if d != dist[u][rem]:
                continue

            for v, w in adj[u]:

                new_rem = rem - 1 if labels[u] == labels[v] else k

                if new_rem <= 0:
                    continue

                nd = d + w

                if nd < dist[v][new_rem]:
                    dist[v][new_rem] = nd
                    heapq.heappush(pq, (nd, v, new_rem))

        ans = min(dist[n - 1][1:])

        return -1 if ans == float("inf") else ans