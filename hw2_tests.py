import data
import hw2
import unittest

# Write your test cases for each part below.

#class TestCases(unittest.TestCase):
# for some reason the testing doesn't work unless this code above is commented out on line 7
# Part 1

class TestCreateRectangle(unittest.TestCase):
    def test_create_rectangle_standard(self):
        point1 = data.Point(2, 2)
        point2 = data.Point(10, 10)
        expected_rectangle = data.Rectangle(data.Point(2, 10), data.Point(10, 2))
        result = hw2.create_rectangle(point1, point2)
        self.assertEqual(result, expected_rectangle)

    def test_create_rectangle_abnormal(self):
        point1 = data.Point(5, 5)
        point2 = data.Point(5, 10)
        expected_rectangle = data.Rectangle(data.Point(5, 10), data.Point(5, 5))
        result = hw2.create_rectangle(point1, point2)
        self.assertEqual(result, expected_rectangle)

    def test_create_rectangle_identical_points(self):
        point1 = data.Point(7, 7)
        point2 = data.Point(7, 7)
        expected_rectangle = data.Rectangle(data.Point(7, 7), data.Point(7, 7))
        result = hw2.create_rectangle(point1, point2)
        self.assertEqual(result, expected_rectangle)

# Part 2

class TestShorterDurationThan(unittest.TestCase):
    def test_shorter_duration_than_true(self):
        duration1 = data.Duration(3, 20)  # 3 minutes, 20 seconds
        duration2 = data.Duration(4, 0)  # 4 minutes, 0 seconds
        result = hw2.shorter_duration_than(duration1, duration2)
        self.assertTrue(result)

    def test_shorter_duration_than_false(self):
        duration1 = data.Duration(5, 0)  # 5 minutes, 0 seconds
        duration2 = data.Duration(4, 30)  # 4 minutes, 30 seconds
        result = hw2.shorter_duration_than(duration1, duration2)
        self.assertFalse(result)

    def test_shorter_duration_than_equal(self):
        duration1 = data.Duration(4, 30)  # 4 minutes, 30 seconds
        duration2 = data.Duration(4, 30)  # 4 minutes, 30 seconds
        result = hw2.shorter_duration_than(duration1, duration2)
        self.assertFalse(result)


# Part 3

class TestSongsShorterThan(unittest.TestCase):
    def test_songs_shorter_than_one_song(self):
        song1 = data.Song("Artist1", "Song1", data.Duration(3, 0))
        song2 = data.Song("Artist2", "Song2", data.Duration(4, 30))
        song3 = data.Song("Artist3", "Song3", data.Duration(5, 0))
        songs = [song1, song2, song3]
        max_duration = data.Duration(4, 0)
        result = hw2.songs_shorter_than(songs, max_duration)
        self.assertEqual(result, [song1])

    def test_songs_shorter_than_no_songs(self):
        song1 = data.Song("Artist1", "Song1", data.Duration(3, 30))
        song2 = data.Song("Artist2", "Song2", data.Duration(2, 45))
        song3 = data.Song("Artist3", "Song3", data.Duration(3, 15))
        songs = [song1, song2, song3]
        max_duration = data.Duration(2, 30)
        result = hw2.songs_shorter_than(songs, max_duration)
        self.assertEqual(result, [])

    def test_songs_shorter_than_all_songs(self):
        song1 = data.Song("Artist1", "Song1", data.Duration(2, 0))
        song2 = data.Song("Artist2", "Song2", data.Duration(3, 0))
        song3 = data.Song("Artist3", "Song3", data.Duration(1, 30))
        songs = [song1, song2, song3]
        max_duration = data.Duration(4, 0)
        result = hw2.songs_shorter_than(songs, max_duration)
        self.assertEqual(result, [song1, song2, song3])

# Part 4
class TestRunningTime(unittest.TestCase):
    def test_running_time_valid_playlist(self):
        song1 = data.Song("Decemberists", "June Hymn", data.Duration(4, 30))
        song2 = data.Song("Broken Bells", "October", data.Duration(3, 40))
        song3 = data.Song("Kansas", "Dust in the Wind", data.Duration(3, 29))
        song4 = data.Song("Local Natives", "Airplanes", data.Duration(3, 58))
        songs = [song1, song2, song3, song4]

        playlist = [0, 2, 1, 3, 0]
        result = hw2.running_time(songs, playlist)
        expected_duration = data.Duration(20, 7)
        self.assertEqual(result, expected_duration)

    def test_running_time_with_out_of_range_indices(self):
        song1 = data.Song("Decemberists", "June Hymn", data.Duration(4, 30))
        song2 = data.Song("Broken Bells", "October", data.Duration(3, 40))
        songs = [song1, song2]

        playlist = [0, 1, 2, -1]  # Includes out-of-range indices
        result = hw2.running_time(songs, playlist)
        expected_duration = data.Duration(8, 10)
        self.assertEqual(result, expected_duration)

    def test_running_time_empty_playlist(self):
        song1 = data.Song("Decemberists", "June Hymn", data.Duration(4, 30))
        songs = [song1]

        playlist = []  # Empty playlist
        result = hw2.running_time(songs, playlist)
        expected_duration = data.Duration(0, 0)
        self.assertEqual(result, expected_duration)

# Part 5
class TestValidateRoute(unittest.TestCase):
    def test_validate_route_valid(self):
        city_links = [
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']
            ]
        route = ['san luis obispo', 'santa margarita', 'atascadero']
        self.assertTrue(hw2.validate_route(city_links, route))

    def test_validate_route_invalid(self):
        city_links = [
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']
        ]
        route = ['san luis obispo', 'atascadero']
        self.assertFalse(hw2.validate_route(city_links, route))

    def test_validate_route_empty(self):
        city_links = [
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']
        ]
        route = []
        self.assertTrue(hw2.validate_route(city_links, route))

    def test_validate_route_single_city(self):
        city_links = [
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']
        ]
        route = ['san luis obispo']
        self.assertTrue(hw2.validate_route(city_links, route))

# Part 6

class TestLongestRepetition(unittest.TestCase):
    def test_longest_repetition_standard_case(self):
        numbers = [1, 1, 2, 2, 1, 1, 1, 3]
        result = hw2.longest_repetition(numbers)
        self.assertEqual(result, 4)

    def test_longest_repetition_multiple_equal_lengths(self):
        numbers = [1, 1, 2, 2, 3, 3]
        result = hw2.longest_repetition(numbers)
        self.assertEqual(result, 0)  # First longest repetition starts at index 0

    def test_longest_repetition_single_element(self):
        numbers = [5]
        result = hw2.longest_repetition(numbers)
        self.assertEqual(result, 0)

    def test_longest_repetition_empty_list(self):
        numbers = []
        result = hw2.longest_repetition(numbers)
        self.assertIsNone(result)

    def test_longest_repetition_entire_list_same_number(self):
        numbers = [2, 2, 2, 2, 2]
        result = hw2.longest_repetition(numbers)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
