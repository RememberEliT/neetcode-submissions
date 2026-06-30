class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        numbers = {}
        for num in nums:
            
            if num in numbers:
                numbers[num] += 1
            else:
                numbers[num] = 1

        key = sorted(numbers.items(), key=lambda item: item[1], reverse=True)

        for i in range(k):
            result.append(key[i][0])
        return list(result)

        

        
