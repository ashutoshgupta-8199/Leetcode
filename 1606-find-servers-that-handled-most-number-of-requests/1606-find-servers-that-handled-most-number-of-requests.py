import heapq

class Solution:
    def busiestServers(self, k, arrival, load):

        # Fenwick Tree: maintains available servers
        bit = [0] * (k + 1)

        def update(i, delta):
            i += 1
            while i <= k:
                bit[i] += delta
                i += i & -i

        def prefix_sum(i):
            # Number of available servers with IDs < i
            result = 0
            while i > 0:
                result += bit[i]
                i -= i & -i
            return result

        def find_kth(target):
            # Find server with the target-th available position
            idx = 0
            step = 1 << (k.bit_length() - 1)

            while step:
                nxt = idx + step

                if nxt <= k and bit[nxt] < target:
                    idx = nxt
                    target -= bit[nxt]

                step >>= 1

            return idx

        # Initially, all servers are available
        for i in range(k):
            update(i, 1)

        busy = []
        count = [0] * k

        for i in range(len(arrival)):

            # Release completed servers
            while busy and busy[0][0] <= arrival[i]:
                free_time, server = heapq.heappop(busy)
                update(server, 1)

            # If all servers are busy, drop the request
            if prefix_sum(k) == 0:
                continue

            preferred = i % k

            # Available servers with IDs < preferred
            before = prefix_sum(preferred)

            # Available servers with IDs >= preferred
            suffix = prefix_sum(k) - before

            if suffix > 0:
                # Select first available server >= preferred
                server = find_kth(before + 1)
            else:
                # Wrap around to the smallest available server
                server = find_kth(1)

            # Mark server as busy
            update(server, -1)

            count[server] += 1

            heapq.heappush(
                busy,
                (arrival[i] + load[i], server)
            )

        max_count = max(count)

        return [
            i for i in range(k)
            if count[i] == max_count
        ]