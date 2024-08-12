import unittest
import uni

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usein = uni.Runner('Усэйн', 10)
        self.andrey = uni.Runner('Андрей', 9)
        self.nick = uni.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for results in dict(cls.all_results).items():
            print(results)

    def test_1(self):
        self.tournament = uni.Tournament(90, self.usein, self.nick)
        self.all_results = self.tournament.start()
        last_place = max(self.all_results.keys())
        self.assertTrue(self.all_results[last_place].name == 'Ник')
    def test_2(self):
        self.tournament = uni.Tournament(90, self.andrey, self.nick)
        self.all_results = self.tournament.start()
        last_place = max(self.all_results.keys())
        self.assertTrue(self.all_results[last_place].name == 'Ник')
    def test_3(self):
        self.tournament = uni.Tournament(90, self. usein, self.andrey, self.nick)
        self.all_results = self.tournament.start()
        last_place = max(self.all_results.keys())
        self.assertTrue(self.all_results[last_place].name == 'Ник')

if __name__ == '__main__':
    unittest.main()


