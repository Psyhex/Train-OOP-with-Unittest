import unittest
from classes import Train, Locomotive, Wagon

train1 = Train("Thomas the spank engine", 2, [Wagon(200, 200, 1000, 1), Wagon(200, 111, 1000, 2)],
               Locomotive(500, 8000, 1))
train2 = Train("Check Engine", 1, [Wagon(200, 200, 1000, 1), Wagon(200, 555, 1000, 2)], Locomotive(600, 8000, 2))


class TestWagonWeight(unittest.TestCase):
    def test_check_if_load_not_over_the_limit(self):
        wagon_weight = Wagon(200, 200, 1000, 1).check_if_load_not_over_the_limit()
        self.assertEqual(wagon_weight, True)

    def test_check_if_load_not_over_the_limit_other(self):
        wagon_weight = Wagon(600, 700, 1000, 2).check_if_load_not_over_the_limit()
        self.assertEqual(wagon_weight, False)


class TestWagonWeightInTrain(unittest.TestCase):
    def test_calculate_wagon_weight(self):
        calculate_wagon_weight = train1.calculate_wagon_weight()
        self.assertEqual(calculate_wagon_weight, 711)


class TestCheckCanTrainMove(unittest.TestCase):
    def test_check_can_train_move(self):
        check_can_train_move = \
            Train("Thomas the spank engine", 2,
                  [Wagon(200, 200, 1000, 1), Wagon(200, 111, 1000, 2)],
                  Locomotive(500, 8000, 1)).check_can_train_move(711)
        self.assertEqual(check_can_train_move, True)

    def test_check_can_train_move_other(self):
        train = \
            Train("Thomas the spank engine", 2,
                  [Wagon(200, 200, 1000, 1), Wagon(200, 111, 1000, 2)],
                  Locomotive(500, 8000, 1))
        self.assertRaises(Exception, train.check_can_train_move, 454654541)


class TestSortTrains(unittest.TestCase):
    def test_sort_trains(self):
        sort_trains = Train.sort_trains([train1, train2])
        self.assertEqual(sort_trains, [train2, train1])


class TestSortLocomotivesByTheirWagonSumMass(unittest.TestCase):
    def test_sort_locomotive_by_their_wagon_sum_mass(self):
        sort_locomotive_by_wagon_sum_mass = Train.sort_locomotive_by_their_wagon_sum_mass([train1, train2])
        self.assertEqual(sort_locomotive_by_wagon_sum_mass, [train1.locomotive, train2.locomotive])
