class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks).values()
        m = max(freq)
        k = sum(1 for v in freq if v == m)
        return max(len(tasks),(n+1) * (m-1)+k)
        