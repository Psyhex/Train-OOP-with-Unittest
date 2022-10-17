from classes import Train, Locomotive, Wagon, Station

wagon1 = Wagon(200, 200, 1000, 1)
wagon2 = Wagon(200, 111, 1000, 2)
wagon3 = Wagon(62, 500, 1000, 3)
if not wagon1.check_if_load_not_over_the_limit():
    raise Exception('Load is over the limit')
wagon2.check_if_load_not_over_the_limit()
wagon3.check_if_load_not_over_the_limit()


locomotive1 = Locomotive(500, 8000, 1)
locomotive2 = Locomotive(5000, 10000, 2)

train1 = Train("Thomas the spank engine", 2, [wagon1, wagon2], locomotive1)
train2 = Train("Check Engine", 1, [wagon3], locomotive2)
print(str(train1))
print(Train.sort_trains([train1, train2]))
train1_wagon_weight = train1.calculate_wagon_weight()
print(f"Wagon weight calculation: {train1_wagon_weight}")

print(train1.check_can_train_move(train1_wagon_weight))

print(Train.sort_locomotive_by_their_wagon_sum_mass([train1, train2]))


train_sort = Train.sort_trains([train1, train2])
print(train_sort)

train_data_to_json = Train.write_to_json(train_sort)

station1 = Station("Vilnius Station", "Vilnius", 5, [train1])
station2 = Station("Klaipeda Station", "Klaipeda", 2, [train2])
print(station1)
print(station2)
train_trip1 = Station.train_trip(train1, station_from=station1, station_to=station2)
train_trip2 = Station.train_trip(train2, station_from=station2, station_to=station1)
print(train_trip1)
print(train_trip2)
