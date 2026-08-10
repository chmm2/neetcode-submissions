class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> ind = new HashMap<>();
        
        for(int i=0; i<nums.length; i++)
        {
            ind.put(nums[i],i);
        }

        for(int i=0; i<nums.length; i++)
        {
            int diff = target - nums[i];
            if(ind.containsKey(diff) && ind.get(diff)!=i)
            {
                return new int[]{i,ind.get(diff)};
            }
        }
        return new int[]{};
    }
}
