main = input().split()
n = int(main[0])
k = int(main[1])

class PQ(object):
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def put(self, data):
        self.queue.append(data)

    def get(self):
        try:
            min = 0
            for i in range(len(self.queue)):
                if self.queue[i] < self.queue[min]:
                    min = i
            point = self.queue[min]
            del self.queue[min]
            return point
        except IndexError:
            exit()


class Graph:
    def __init__(self, n):
        self.v = n
        self.e = [[-1 for i in range(n)] for j in range(n)]
        self.vis = []
        self.castles = []

    def add_path(self, a, b, dist):
        self.e[a][b] = dist
        self.e[b][a] = dist

    def dijkstra(self, start):
        self.vis = []
        D = {v:float('inf') for v in range(self.v)}
        D[start] = 0

        pq = PQ()
        pq.put((0, start))

        while not pq.is_empty():
            (dist, current_v) = pq.get()
            self.vis.append(current_v)

            for i in range(self.v):
                if self.e[current_v][i] != -1:
                    distance = self.e[current_v][i]
                    if i not in self.vis:
                        old_cost = D[i]
                        new_cost = D[current_v] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, i))
                            D[i] = new_cost
        return D

    def add_castle(self, coor):
        self.castles.append(coor)

    def count_needs(self):
        needs = 0
        for i in self.castles:
            d = self.dijkstra(i)
            for j in self.castles:
                needs += d[j]
        print(needs)

kingdom = Graph(n)
kingdom.add_castle(0)

for i in range(n-1):
    l = input().split()
    kingdom.add_path(int(l[0])-1, int(l[1])-1, int(l[2]))

for i in range(k):
    kingdom.add_castle(int(input())-1)
    kingdom.count_needs()
