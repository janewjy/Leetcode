class Solution(object):

    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        cur_min_ind = 1
        cur_max_ind = min(len(nums) - 1, nums[0])
        num_steps = 0

        while cur_min_ind < len(nums):
            cur_min_ind, cur_max_ind = cur_max_ind + 1, min(
                len(nums) - 1, max([
                ind + nums[ind]
                for ind in range(cur_min_ind, cur_max_ind + 1)]))
            num_steps += 1


        return num_steps

if __name__ == '__main__':
    # print Solution().jump([1])
    # print Solution().jump([1, 2])
    # print Solution().jump([1, 2, 3])
    # print Solution().jump([1, 2, 3, 4])
    # print Solution().jump([1, 1, 1, 1, 1])
    print Solution().jump([2, 1])
