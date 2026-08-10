class Solution:
    def foreignDictionary(self, words):

        # all unique characters
        chars = set()
        for w in words:
            chars.update(w)

        adj = {c: set() for c in chars}
        indegree = {c: 0 for c in chars}

        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]

            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break

        q = deque()

        for c in chars:
            if indegree[c] == 0:
                q.append(c)

        ans = []

        while q:
            cur = q.popleft()
            ans.append(cur)

            for nxt in adj[cur]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)

        if len(ans) != len(chars):
            return ""

        return "".join(ans)