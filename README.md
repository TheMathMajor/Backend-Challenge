# Backend Coding Challenge

## Description
### Shifted List Search
We want to find the maximum element of a sorted list that has been sliced with the 2 pieces swapped.  I used a binary search algorithm to accomplish this task.
### Most Occurring Triplets
Given a list of user activity on a website, we want to find the top 10 most occuring "triplets".  A triplet is a unique group of three consecutive pages visited by the same user.

## Technical Details
### Shifted List Search
I implemented a binary search algorithm so the order of growth is logarithmic.  The function asserts that the list has to be non-empty.  Possible edge cases are empty lists and sorted lists, both of which are handled.  If there were 1 million elements in our list, then it would take log(1000000) = 20 operations to find the maximum.

### Most Occurring Triplets
I used a dictionary (hash table) to keep track of a consecutive list of user activity and another dictionary to keep track of the frequencies of unique consecutive triples.  I then sorted the dictionary of the frequencies of unique consecutive triples and returned the top 10 most frequent occurring triples.

## Link
[https://github.com/TheMathMajor/Android-Challenge](https://github.com/TheMathMajor/Backend-Challenge)