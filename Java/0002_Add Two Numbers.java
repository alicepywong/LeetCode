class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] res = new int[2];

        for (int i = 0; i < nums.length; i++) {
            for (int j = i; j < nums.length - 1; j++) {
                int sum = nums[i] + nums[j+1];
                if (sum == target) {
                    res[0] = i;
                    res[1] = j + 1;
                    break;
                }
            }
        }
        return res;
    }
}