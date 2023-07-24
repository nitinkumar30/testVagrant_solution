# Problem statement

> Create an in-memory store for recently played songs that can accommodate N songs per user, with a fixed initial capacity.  
> This store must have the capability to store a list of song-user pairs, with each song linked to a user.  
> It should also be able to fetch recently played songs based on the user and eliminate the least recently played songs when the store becomes full.  


# Example

> Illustration, when 4 different songs were played by a user & Initial capacity is 3:  

Let's assume that the user has played 3 songs - S1, S2 and S3.
- The playlist would look like -> S1,S2,S3
- When S4 song is played -> S2,S3,S4 
- When S2 song is played -> S3,S4,S2 
- When S1 song is played -> S4,S2,S1


# Code explanation

Here's a step-by-step explanation of the code using the provided example:

1. We start by importing the `defaultdict` and `deque` classes from the collections module. These classes will be used to implement the in-memory store.
2. We define a class called `RecentlyPlayedStore` that represents the in-memory store for recently played songs. The class has an __init__ method that takes a capacity parameter, which determines the maximum number of songs that can be stored per user. It also initializes an empty defaultdict called store to store the songs for each user.
3. The `add_song` method is defined to add a new song to the store for a given user. It takes two parameters: user and song. 
4. If the number of songs for that user exceeds the capacity, the least recently played song is removed using `popleft()` from the deque associated with that user. The new song is then added to the deque.
5. The `get_recently_played_songs` method is defined to retrieve the recently played songs for a given user. It takes one parameter: user. It returns a list of songs stored in the deque associated with that user.
6. We create an instance of the `RecentlyPlayedStore` class called store with a capacity of 3.
7. We add songs to the store using the `add_song` method. In the provided example, we add songs for two different users: "user1" and "user2". The songs are added in the order specified in the example.
8. Finally, we use the `get_recently_played_songs` method to retrieve the recently played songs for each user. We pass the user as an argument to the method. In the example, we retrieve the recently played songs for "user1" and "user2" and print the results.

Here's how the example would be executed:

1. Initially, the playlist is empty.
2. When the song "S1" is played, it is added to the playlist: ["S1"].
3. When the song "S2" is played, it is added to the playlist, and the oldest song "S1" is removed: ["S2", "S1"].
4. When the song "S3" is played, it is added to the playlist, and the oldest song "S2" is removed: ["S3", "S1"].
5. When the song "S4" is played, it is added to the playlist, and the oldest song "S1" is removed: ["S4", "S3", "S1"].
6. When the song "S2" is played again, it is added to the playlist, and the oldest song "S3" is removed: ["S2", "S4", "S3"].
7. When the song "S1" is played again, it is added to the playlist, and the oldest song "S4" is removed: ["S1", "S2", "S4"].

Here's how we can run tests to validate the logic behind the solution:

1. We define a function called `test_recently_played_store` that contains a series of assertions to validate the logic of the `RecentlyPlayedStore` class. Each assertion compares the actual output of a method call with the expected output.
2. We create a `RecentlyPlayedStore` instance, add songs, retrieve recently played songs, and compare the results with the expected values. If all the assertions pass, the message "All tests passed!" is printed.
3. You can run the `test_recently_played_store` function to execute the tests and verify that the code behaves as expected. If any of the assertions fail, an AssertionError will be raised, indicating that there is an issue with the code.

# Author

[Nitin Kumar](https://linkedin.com/in/nitin30kumar/)
