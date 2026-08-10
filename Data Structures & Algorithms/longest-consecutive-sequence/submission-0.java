class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> num = new HashSet<>();
        for(int n:nums)
        {
            num.add(n);
        }

        int longest = 0;

        for(int n:num)
        {
            if(!num.contains(n-1))
            {
                int length = 1;
                while(num.contains(n+length))
                {
                    length++;
                }
                longest = Math.max(longest,length);
            }

        }
        return longest;
    }
}
