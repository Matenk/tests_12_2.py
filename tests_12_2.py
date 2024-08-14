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

        result_name = {place: runner.name for place, runner in cls.all_results.items()}
        print(f'{result_name}')
        # for results in cls.all_results.items():
        #     print(results)

    def test_1(self):
        self.tournament = uni.Tournament(90, self.usein, self.nick)
        self.results = self.tournament.start()
        self.all_results.update(self.results)
        last_place = max(self.results.keys())
        self.assertTrue(self.results[last_place].name == 'Ник')
        self.tearDownClass()

    def test_2(self):
        self.tournament = uni.Tournament(90, self.andrey, self.nick)
        self.results = self.tournament.start()
        self.all_results.update(self.results)
        last_place = max(self.results.keys())
        self.assertTrue(self.results[last_place].name == 'Ник')
        self.tearDownClass()

    def test_3(self):
        self.tournament = uni.Tournament(90, self. usein, self.andrey, self.nick)
        self.results = self.tournament.start()
        self.all_results.update(self.results)
        last_place = max(self.results.keys())
        self.assertTrue(self.results[last_place].name == 'Ник')


if __name__ == '__main__':
    unittest.main()
