class Solution:
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)

        if px == py:
            return

        # Whichever email is alphabetically smaller, becomes the parent
        if px < py:
            self.parent[py] = px
        else:
            self.parent[px] = py

    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        nodes = defaultdict(set)
        email_names = {}
        for i, account in enumerate(accounts):
            name, *emails = account

            for email in emails:
                nodes[email].add(i)
                email_names[email] = name

        # print(nodes)
        self.parent = {x: x for x in nodes}
        for account in accounts:
            name, *emails = account

            for i in range(1, len(emails)):
                self.union(emails[0], emails[i])
        # print(self.parent)

        common_nodes = defaultdict(list)
        for node in nodes:
            pnode = self.find(node)
            common_nodes[pnode].append(node)

        answers = []
        for pnode in common_nodes:
            name = email_names[pnode]
            answer = [name] + sorted(common_nodes[pnode])
            answers.append(answer)

        return answers
