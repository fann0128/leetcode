from typing import List
class Solution:
    @classmethod
    def hIndex(self, citations: List[int]) -> int:
        citation_dict = {}
        for citation in citations :
            for i in range(citation + 1) :
                if i in citation_dict.keys() :
                    citation_dict[i] += 1
                else :
                    citation_dict[i] = 1
        # print(citation_dict)
        for i in reversed(range(len(citations)+1)):
            if i in citation_dict.keys():
                if citation_dict[i] >= i :
                    return i
        return 0

print(Solution.hIndex(citations=[1,3,1]))