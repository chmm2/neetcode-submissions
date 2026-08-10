class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Stack<Integer> stack = new Stack<>();
        int[] result = new int[temperatures.length];
        for(int i=0; i<temperatures.length; i++)
        {
            if(stack.isEmpty() || temperatures[stack.peek()]>=temperatures[i])
            {
                stack.push(i);
            }
            else
            {
                if(temperatures[stack.peek()]<temperatures[i])
                {
                    while(!stack.isEmpty() && temperatures[stack.peek()]<temperatures[i])
                    {
                        int r = stack.pop();
                        result[r] = i-r;
                    }
                    stack.push(i);
                }
            }
        }

        if(!stack.isEmpty())
        {
            while(!stack.isEmpty())
            {
                int r = stack.pop();
                result[r] = 0;
            }
        }
        return result;
    }
}
