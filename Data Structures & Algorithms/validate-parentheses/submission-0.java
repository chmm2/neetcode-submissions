class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> opp = new HashMap<>();
        opp.put(')','(');
        opp.put(']','[');
        opp.put('}','{');

        for(char c: s.toCharArray())
        {
            if(!stack.isEmpty() && stack.peek()==opp.get(c))
            {
                stack.pop();
            }
            else
            {
                stack.push(c);
            }
        }
        return stack.isEmpty();
    }
}
