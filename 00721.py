# https://leetcode.com/problems/accounts-merge/
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

            for j, email in enumerate(emails):
                nodes[email].add(i)
                email_names[email] = name

        # print(nodes)
        reverse_nodes = defaultdict(set)
        for node in nodes:
            for account in nodes[node]:
                reverse_nodes[account].add(node)

        # print(reverse_nodes)
        # print(email_names)

        edges = set()
        for node in nodes:
            all_other_emails = set()
            for account in nodes[node]:
                all_other_emails.update(reverse_nodes[account])
            all_other_emails.discard(node)

            for email in all_other_emails:
                if (email, node) not in edges:
                    edges.add((node, email))

        # print(edges)

        self.parent = {x: x for x in nodes}
        for e1, e2 in edges:
            self.union(e1, e2)

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
