import heapq

class Twitter:

    def __init__(self):
        self.users = collections.defaultdict(list)
        self.time = 1
        self.followers = collections.defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.users[userId].append((self.time, tweetId))
        self.time += 1        

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        for user in [userId] + list(self.followers[userId]):
            tweets.extend(self.users[user][-10:])
        heapq.heapify(tweets)
        recent_tweets = [tweetId for _, tweetId in heapq.nlargest(10, tweets)]
        return recent_tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)