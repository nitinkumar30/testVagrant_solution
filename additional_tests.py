def test_recently_played_store():
    # Test Case 1: Adding songs for a single user
    # Steps:
    # 1. Create a RecentlyPlayedStore with a capacity of 3
    # 2. Add songs for user "user"
    # 3. Retrieve recently played songs for user "user"
    # 4. Compare the results with the expected values
    store = RecentlyPlayedStore(3)
    store.add_song("user", "S1")
    store.add_song("user", "S2")
    store.add_song("user", "S3")
    assert store.get_recently_played_songs("user") == ["S1", "S2", "S3"]

    # Test Case 2: Adding songs for multiple users
    # Steps:
    # 1. Create a RecentlyPlayedStore with a capacity of 3
    # 2. Add songs for user "user1"
    # 3. Add songs for user "user2"
    # 4. Retrieve recently played songs for user "user1"
    # 5. Retrieve recently played songs for user "user2"
    # 6. Compare the results with the expected values
    store = RecentlyPlayedStore(3)
    store.add_song("user1", "S1")
    store.add_song("user1", "S2")
    store.add_song("user2", "S3")
    store.add_song("user2", "S4")
    assert store.get_recently_played_songs("user1") == ["S1", "S2"]
    assert store.get_recently_played_songs("user2") == ["S3", "S4"]

    # Test Case 3: Adding songs exceeding the capacity
    # Steps:
    # 1. Create a RecentlyPlayedStore with a capacity of 2
    # 2. Add songs for user "user"
    # 3. Retrieve recently played songs for user "user"
    # 4. Compare the results with the expected values
    store = RecentlyPlayedStore(2)
    store.add_song("user", "S1")
    store.add_song("user", "S2")
    store.add_song("user", "S3")
    assert store.get_recently_played_songs("user") == ["S2", "S3"]

    # Test Case 4: Adding previously played songs
    # Steps:
    # 1. Create a RecentlyPlayedStore with a capacity of 3
    # 2. Add songs for user "user"
    # 3. Add a previously played song for user "user"
    # 4. Retrieve recently played songs for user "user"
    # 5. Compare the results with the expected values
    store = RecentlyPlayedStore(3)
    store.add_song("user", "S1")
    store.add_song("user", "S2")
    store.add_song("user", "S3")
    store.add_song("user", "S2")
    assert store.get_recently_played_songs("user") == ["S1", "S3", "S2"]

    print("All tests passed!")

# Run the tests
test_recently_played_store()
