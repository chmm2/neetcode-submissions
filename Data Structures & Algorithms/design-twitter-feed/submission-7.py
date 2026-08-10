from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        self.time = 0
        self.followMap = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        self.tweets[userId].append((self.time,tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        n = len(self.tweets[userId])
        temp = [x for x in self.tweets[userId]]
        for f in self.followMap[userId]:
            temp.extend(self.tweets[f])
        temp.sort(reverse=True)

        return [tweetId for _, tweetId in temp[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return 
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].discard(followeeId)