class Solution:
    def countBits(self, n: int) -> List[int]:
        llist = []
        for i in range(n+1):
            a = bin(i)
            summ = 0
            for j in a[2:]:
                summ += int(j)
            llist.append(summ)
        return llist