#Given an array of integers,
#return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution.
#Example:
#Given nums = [2, 7, 11, 15], target = 9,
#Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].

def twosum(nums,target):
   result = {}
   for i in range(0,len(nums),1):
       for j in range(1,len(nums),1):
           if(nums[i]+nums[j] == target):
               result = [i,j]
               return result  
        
print twosum([1,2,5,8,10],6);




def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            print buff_dict
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i+1]
            else:
                buff_dict[target - nums[i]] = i+1
        
print twoSum([77,7,11,2],9);

