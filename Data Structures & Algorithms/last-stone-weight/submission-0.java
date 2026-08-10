class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        for(int s: stones)
        {
            minHeap.offer(-s);
        }

        while(minHeap.size()>1)
        {
            int first  = minHeap.poll();
            int second = minHeap.poll();
            if(second>first)
            {
                minHeap.offer(first-second);
            }
        }
        return (minHeap.size()==0) ? 0 : Math.abs(minHeap.peek());
    }
}
