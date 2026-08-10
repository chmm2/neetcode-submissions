class Solution {

    public String encode(List<String> strs) {
        if(strs.isEmpty()) return "";
        StringBuilder res = new StringBuilder();
        List<Integer> sizes = new ArrayList<>();
        for(String str: strs)
        {
            sizes.add(str.length());
        }

        for(int size: sizes)
        {
            res.append(size).append(',');
        }
        res.deleteCharAt(res.length() - 1); // remove last comma
        res.append('#');
        for(String str: strs)
        {
            res.append(str);
        }
        return res.toString();
    }

    public List<String> decode(String str) {
        if(str.length()==0)
        {
            return new ArrayList<>();
        }

        List<String> res = new ArrayList<>();
        int i=0;
        while(str.charAt(i)!='#')
        {
            i++;    
        }
        String numbers = str.substring(0,i);
        String[] length = numbers.split(",");
        int start = i + 1;

        for(String len : length) 
        {

            int l = Integer.parseInt(len);
            res.add(str.substring(start, start + l));
            start += l;
        }
        return res;
    }
}
