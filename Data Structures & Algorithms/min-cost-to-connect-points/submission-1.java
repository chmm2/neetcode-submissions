class Solution {
    public int manDist(int[][] points, int p1, int p2)
    {
        return Math.abs(points[p1][0]-points[p2][0]) + Math.abs(points[p1][1]-points[p2][1]);
    }

    public int minCostConnectPoints(int[][] points) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b) -> a[0]-b[0]);

        boolean[] set = new boolean[points.length];
        int cost = 0;

        pq.offer(new int[]{0,0});

        while(!pq.isEmpty())
        {
            int[] p = pq.poll();
            int wt = p[0];
            int node = p[1];

            if(set[node]) continue;

            set[node] = true;
            cost += wt;

            for(int i=0; i<points.length; i++)
            {
                if(!set[i])
                {
                    int weight = manDist(points, node, i);
                    pq.offer(new int[]{weight,i});
                }
            }

        }
        return cost;
    }
}
