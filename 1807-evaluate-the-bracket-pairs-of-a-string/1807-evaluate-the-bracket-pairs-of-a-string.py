import re

class Solution:
    def evaluate(self, s, knowledge):
        m = dict(knowledge)

        words = re.split(r'[()]', s)

        out = []
        for i, w in enumerate(words):
            if i % 2 == 0:
                out.append(w)
            else:
                out.append(m.get(w, "?"))

        return "".join(out)
        