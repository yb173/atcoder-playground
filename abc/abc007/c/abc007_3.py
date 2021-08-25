from collections import deque

class Maze:
    def __init__(self, H: int, W: int, S: list, sh: int, sw: int) -> None:
        self.cost = [[-1] * W for _ in range(H)]
        self.cost[sh][sw] = 0
        
        # 深さ優先探索
        self.__bfs(H, W, S, sh, sw)
        
    def __bfs(self, H: int, W: int, S: list, sh: int, sw: int) -> None:
        q = deque([(sh, sw)])
        while len(q) > 0:
            h, w = q.popleft()
            for dh, dw in [(h + 1, w), (h - 1, w), (h, w + 1), (h, w - 1)]:
                if not (0 <= dh < H and 0 <= dw < W):
                    continue
                if S[dh][dw] == "#":
                    continue
                if self.cost[dh][dw] == -1:
                    self.cost[dh][dw] = self.cost[h][w] + 1
                    q.append((dh, dw))
    
    def get_cost(self):
        return self.cost

R, C = map(int, input().split())
sy, sx = map(int, input().split())
sy -= 1
sx -= 1
gy, gx = map(int, input().split())
gy -= 1
gx -= 1

S = [input() for _ in range(R)]

maze = Maze(R, C, S, sy, sx)
cost = maze.get_cost()

print(cost[gy][gx])
