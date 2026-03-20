from typing import List
from collections import Counter

#function
def topKfrequntele(nums: List[int], k: int) -> List[int]:
    
    frequent = Counter(nums)

    sorted_nums = sorted(frequent.items(), key=lambda x: (-x[1], x[0]))

    result = [num for num, count in sorted_nums[:k]]

    return result

if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    k = int(input("Enter value of k: "))
    
    #function call
print("Top k frequent elements: ", topKfrequntele(nums, k))
