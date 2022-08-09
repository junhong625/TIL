class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(len(temperatures)-1):
            cnt = 1
            for j in range(i+1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    result.append(cnt)
                    break
                else:
                    cnt += 1
            else:
                result.append(0)
        result.append(0)
        return result