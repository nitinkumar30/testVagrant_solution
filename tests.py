def test_recently_played_store():
    # Create a RecentlyPlayedStore with a capacity of 3
    store = RecentlyPlayedStore(3)

    # Add songs for user "user"
    store.add_song("user", "S1")
    store.add_song("user", "S2")
    store.add_song("user", "S3")

    # Retrieve recently played songs for user "user"
    assert store.get_recently_played_songs("user") == ["S1", "S2", "S3"]

    # Add another song for user "user"
    store.add_song("user", "S4")

    # Retrieve recently played songs for user "user"
    assert store.get_recently_played_songs("user") == ["S2", "S3", "S4"]

    # Add a previously played song for user "user"
    store.add_song("user", "S2")

    # Retrieve recently played songs for user "user"
    assert store.get_recently_played_songs("user") == ["S3", "S4", "S2"]

    # Add another previously played song for user "user"
    store.add_song("user", "S1")

    # Retrieve recently played songs for user "user"
    assert store.get_recently_played_songs("user") == ["S4", "S2", "S1"]

    print("All tests passed!")

# Run the tests
test_recently_played_store()
