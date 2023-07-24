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

# Example usage:
store = RecentlyPlayedStore(3)

store.add_song("user", "S1")
store.add_song("user", "S2")
store.add_song("user", "S3")

print(store.get_recently_played_songs("user"))  
# Output: ['S1', 'S2', 'S3']

store.add_song("user", "S4")
print(store.get_recently_played_songs("user"))  
# Output: ['S2', 'S3', 'S4']

store.add_song("user", "S2")
print(store.get_recently_played_songs("user"))  
# Output: ['S3', 'S4', 'S2']

store.add_song("user", "S1")
print(store.get_recently_played_songs("user"))  
# Output: ['S4', 'S2', 'S1']
