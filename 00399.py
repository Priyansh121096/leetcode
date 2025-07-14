# https://leetcode.com/problems/evaluate-division/description/
class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        adj = defaultdict(list)
        for i in range(len(equations)):
            a, b = equations[i]
            val = values[i]

            adj[a].append((b, val))
            adj[b].append((a, 1 / val))

        answers = []
        for a, b in queries:
            # print(a, b, answers)
            # if a == b:
            #     answers.append(1)
            #     continue

            if a not in adj or b not in adj:
                answers.append(-1)
                continue

            q, v = deque([(a, 1)]), set()

            while q:
                node, val = q.popleft()
                v.add(node)

                if node == b:
                    answers.append(val)
                    break

                for n, nval in adj[node]:
                    if n not in v:
                        q.append((n, val*nval))
            else:
                answers.append(-1)

        return answers
