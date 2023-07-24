from collections import defaultdict, deque

class RecentlyPlayedStore:
    def __init__(self, capacity):
        self.capacity = capacity
        self.store = defaultdict(deque)

    def add_song(self, user, song):
        if len(self.store[user]) == self.capacity:
            self.store[user].popleft()
        self.store[user].append(song)

    def get_recently_played_songs(self, user):
        return list(self.store[user])


store = RecentlyPlayedStore(3)

store.add_song("user1", "song1")
store.add_song("user1", "song2")
store.add_song("user1", "song3")
store.add_song("user1", "song4")

store.add_song("user2", "song5")
store.add_song("user2", "song6")

print(store.get_recently_played_songs("user1"))  
# Output: ['song2', 'song3', 'song4']

print(store.get_recently_played_songs("user2"))  
# Output: ['song5', 'song6']
