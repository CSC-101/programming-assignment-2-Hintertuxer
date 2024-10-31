import data

# Write your functions for each part in the space below.

# Part 1

def create_rectangle(point1: data.Point, point2: data.Point) -> data.Rectangle:
    """
    Creates a Rectangle based on two points by determining the top-left and
    bottom-right corners based on the left-most, right-most, highest, and
    lowest coordinates.

    Inputs:
        - point1 (Point): A point representing one corner of the rectangle.
        - point2 (Point): A point representing the opposite corner of the rectangle.

    Output:
        - Rectangle: A Rectangle object with calculated top-left and bottom-right corners.
    """
    # Determine the coordinates for the top-left corner
    x_min = min(point1.x, point2.x)
    y_max = max(point1.y, point2.y)
    top_left = data.Point(x_min, y_max)

    # Determine the coordinates for the bottom-right corner
    x_max = max(point1.x, point2.x)
    y_min = min(point1.y, point2.y)
    bottom_right = data.Point(x_max, y_min)

    # Return a new Rectangle object using these corners
    return data.Rectangle(top_left, bottom_right)
# testing below
"""
point1 = data.Point(2, 2)
point2 = data.Point(10, 10)
rectangle = create_rectangle(point1, point2)
print(rectangle)  # Expected output: Rectangle(Point(2, 10), Point(10, 2))
"""
# Part 2

def shorter_duration_than(duration1: data.Duration, duration2: data.Duration) -> bool:
    """
    Determines if the first duration is shorter than the second duration.

    Inputs:
        - duration1 (Duration): The first duration to compare.
        - duration2 (Duration): The second duration to compare.

    Output:
        - bool: True if the first duration is shorter than the second, False otherwise.
    """
    # Calculate total seconds for each duration
    total_seconds1 = duration1.minutes * 60 + duration1.seconds
    total_seconds2 = duration2.minutes * 60 + duration2.seconds

    # Compare the total seconds
    return total_seconds1 < total_seconds2
# testing below
"""
duration1 = data.Duration(3, 20)  # 3 minutes, 20 seconds
duration2 = data.Duration(4, 0)   # 4 minutes, 0 seconds
print(shorter_duration_than(duration1, duration2))  # Expected output: True

"""

# Part 3

def songs_shorter_than(songs: list[data.Song], max_duration: data.Duration) -> list[data.Song]:
    """
    Returns a list of songs with a duration shorter than the specified max_duration.

    Inputs:
        - songs (list[Song]): A list of Song objects to filter.
        - max_duration (Duration): The upper bound on song length.

    Output:
        - list[Song]: A list of songs that are shorter than max_duration.
    """
    return [song for song in songs if shorter_duration_than(song.duration, max_duration)]
# some more tests
"""
song1 = data.Song("Artist1", "Song1", data.Duration(3, 0))   # 3 minutes, 0 seconds
song2 = data.Song("Artist2", "Song2", data.Duration(4, 30))  # 4 minutes, 30 seconds
song3 = data.Song("Artist3", "Song3", data.Duration(5, 0))   # 5 minutes, 0 seconds
songs = [song1, song2, song3]

max_duration = data.Duration(4, 0)  # 4 minutes, 0 seconds
print(songs_shorter_than(songs, max_duration))  # Expected output: [song1]
"""

# Part 4

def running_time(songs: list[data.Song], playlist: list[int]) -> data.Duration:
    """
    Computes the total running time of songs specified in the playlist indices,
    returning the duration in a properly formatted Duration object.

    Inputs:
        - songs (list[Song]): A list of Song objects.
        - playlist (list[int]): A list of integers representing indices in the songs list.

    Output:
        - Duration: A Duration object representing the total running time of the playlist.
    """
    total_seconds = 0

    # Calculate the total time in seconds by iterating through the playlist
    for index in playlist:
        if 0 <= index < len(songs):  # Ensure the index is in range
            song_duration = songs[index].duration
            total_seconds += song_duration.minutes * 60 + song_duration.seconds

    # Convert total seconds to minutes and seconds
    total_minutes = total_seconds // 60
    remaining_seconds = total_seconds % 60

    # Return the total duration as a Duration object
    return data.Duration(total_minutes, remaining_seconds)
"""
song1 = data.Song("Decemberists", "June Hymn", data.Duration(4, 30))
song2 = data.Song("Broken Bells", "October", data.Duration(3, 40))
song3 = data.Song("Kansas", "Dust in the Wind", data.Duration(3, 29))
song4 = data.Song("Local Natives", "Airplanes", data.Duration(3, 58))
songs = [song1, song2, song3, song4]

playlist = [0, 2, 1, 3, 0]
print(running_time(songs, playlist))  # Expected output: Duration(20, 7)
"""

# Part 5

def validate_route(city_links: list[list[str]], route: list[str]) -> bool:
    """
    Validates whether a route is connected based on provided city links.

    Inputs:
        - city_links (list[list[str]]): A list of city links where each link is a list of two strings.
        - route (list[str]): A list of city names representing the route to validate.

    Output:
        - bool: True if the route is valid (connected by links), False otherwise.
    """
    # An empty route or a single-city route is always valid
    if len(route) <= 1:
        return True

    # Check if each consecutive city pair in the route has a valid link
    for i in range(len(route) - 1):
        city1 = route[i]
        city2 = route[i + 1]

        # Check if there is a link between city1 and city2 in either direction
        if [city1, city2] not in city_links and [city2, city1] not in city_links:
            return False  # No link found for a consecutive city pair

    return True  # All consecutive city pairs have valid links
"""
city_links = [
    ['san luis obispo', 'santa margarita'],
    ['san luis obispo', 'pismo beach'],
    ['atascadero', 'santa margarita'],
    ['atascadero', 'creston']
]

route1 = ['san luis obispo', 'santa margarita', 'atascadero']
route2 = ['san luis obispo', 'atascadero']
print(validate_route(city_links, route1))  # Expected output: True
print(validate_route(city_links, route2))  # Expected output: False
"""

# Part 6

from typing import Optional
def longest_repetition(numbers: list[int]) -> Optional[int]:
    """
    Finds the starting index of the longest contiguous repetition of a single number in the list.

    Inputs:
        - numbers (list[int]): A list of integers.

    Output:
        - Optional[int]: The starting index of the longest contiguous repetition,
                         or None if the list is empty.
    """
    # Handle the case of an empty list
    if not numbers:
        return None

    # Initialize variables to track the longest sequence
    longest_length = 0
    longest_start_index = 0

    # Initialize variables to track the current sequence
    current_num = numbers[0]
    current_length = 1
    current_start_index = 0

    # Iterate over the list starting from the second element
    for i in range(1, len(numbers)):
        if numbers[i] == current_num:
            # Continue the current sequence
            current_length += 1
        else:
            # Check if the current sequence is the longest so far
            if current_length > longest_length:
                longest_length = current_length
                longest_start_index = current_start_index

            # Reset for the new number
            current_num = numbers[i]
            current_length = 1
            current_start_index = i

    # Final check for the last sequence in the list
    if current_length > longest_length:
        longest_start_index = current_start_index

    return longest_start_index

"""
numbers = [1, 1, 2, 2, 1, 1, 1, 3]
print(longest_repetition(numbers))  # Expected output: 4 (start of three 1s)
"""
