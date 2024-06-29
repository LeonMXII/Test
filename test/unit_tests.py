import unittest

from main import solution, discriminant, solve, check_age

class TestMain(unittest.TestCase):
    def test_discriminant(self):
        for i, (a, b, c, expected) in enumerate([
            (1, 2, 1, 0),
            (1, 3, 1, 5)
        ]):
            with self.subTest(i):
                result = discriminant(a, b, c)
                self.assertEqual(expected, result)

    def test_solution(self):
        for i, (a, b, c, expected, expected) in enumerate([
            (1, 8, 15, -3.0, -5.0),
            (1, -13, 12, 1.0, 7.0),
            (-4, 28, -49, 3.5, None),
            (1, 1, 1, "корней нет", None)
        ]):
            with self.subTest(i):
                result = solution(a, b, c)
                self.assertEqual(expected, expected, result)

    def test_solve(self):
        for i, (hare_distances, turtle_distances, expected) in enumerate([
            ([8, 5, 3, 2, 0, 1, 1], [3, 3, 3, 3, 3, 3, 3], "черепаха"),
            ([8, 5, 3, 2, 2, 1, 1], [3, 3, 3, 3, 3, 3, 3], "заяц"),
            ([8, 5, 3, 2, 1, 1, 1], [3, 3, 3, 3, 3, 3, 3], "одинаково")
        ]):
            with self.subTest(i):
                result = solve(hare_distances, turtle_distances)
                self.assertEqual(expected, result)

    def test_check_age(self):
        for i, (age, expected) in enumerate([
            (10, "Доступ запрещён"),
            (18, "Доступ разрешён"),
            (15, "Доступ запрещён")
        ]):
            with self.subTest(i):
                result = check_age(age)
                self.assertEqual(expected, result)

if __name__ == "__main__":
    unittest.main()
