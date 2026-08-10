from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        self.time = 0
        self.followMap = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time,tweetId))
        self.time-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []
        self.followMap[userId].add(userId)
        for follower in self.followMap[userId]:
            if follower in self.tweets:
                index = len(self.tweets[follower]) - 1
                time, tweetId = self.tweets[follower][index]
                heap.append([time, tweetId, follower, index-1])

        heapq.heapify(heap)
        while heap and len(res)<10:
            time,tweetId,follower,index = heapq.heappop(heap)
            res.append(tweetId)
            if index>=0:
                time, tweetId = self.tweets[follower][index]
                heapq.heappush(heap, [time, tweetId, follower, index-1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return 
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].discard(followeeId)