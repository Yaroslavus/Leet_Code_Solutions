class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d,target_list = {}, []
        for i, item in enumerate(nums):
            if item not in d.keys():
                d[item] = i
            else:
                if item*2 == target:
                    return [d[item], i]
        if not target%2 and target/2 in d.keys():
            del d[target//2]
        nums_diff = [target - item for item in nums]
        for item in nums_diff:
            if item in d.keys():
                target_list.append(d[item])
        return sorted(target_list)