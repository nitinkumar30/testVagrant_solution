class RecentlyPlayedStore:
    def __init__(self, capacity):
        self.capacity = capacity
        self.store = {}

    def add_song(self, user, song):
        if user not in self.store:
            self.store[user] = []
        self.store[user].append(song)
        if len(self.store[user]) > self.capacity:
            self.store[user].pop(0)

    def get_recently_played_songs(self, user):
        return self.store.get(user, [])





store = RecentlyPlayedStore(3)

store.add_song("user1", "song1")
store.add_song("user1", "song2")
store.add_song("user1", "song3")
store.add_song("user1", "song4")

store.add_song("user2", "song5")
store.add_song("user2", "song6")
store.add_song("user2", "song7")
store.add_song("user2", "song8")
store.add_song("user2", "song9")
store.add_song("user2", "song10")
store.add_song("user2", "song11")
store.add_song("user2", "song12")

print(store.get_recently_played_songs("user1"))  
# Output: ['song2', 'song3', 'song4']

print(store.get_recently_played_songs("user2"))  
# Output: ['song5', 'song6']
