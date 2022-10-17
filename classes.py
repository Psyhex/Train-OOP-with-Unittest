import json


class Wagon:
    def __init__(self, wagon_mass: float, load: float, max_mass: float, wagon_id: int):
        self.wagon_mass = wagon_mass
        self.load = load
        self.max_mass = max_mass
        self.wagon_id = wagon_id

    def __repr__(self):
        return f"wagon mass: {self.wagon_mass}, load: {self.load}, max mass: {self.max_mass}, wagon id: {self.wagon_id}"

    def check_if_load_not_over_the_limit(self):
        return self.load + self.wagon_mass <= self.max_mass


class Locomotive:
    def __init__(self, locomotive_mass: float, max_towable_mass: float, locomotive_id: int):
        self.locomotive_mass = locomotive_mass
        self.max_towable_mass = max_towable_mass
        self.locomotive_id = locomotive_id

    def __repr__(self):
        return f"loco mass: {self.locomotive_mass}, loco max towable mass: {self.max_towable_mass}," \
               f" id: {self.locomotive_id}, "


class Train:
    def __init__(self, train_name: str, train_id: int, wagons: list[Wagon], locomotive: Locomotive):
        """Class Train Constructor"""
        self.train_name = train_name
        self.train_id = train_id
        self.wagons = wagons
        self.locomotive = locomotive

    def __repr__(self):
        return f"{self.train_name}, {self.train_id}, {self.wagons}, {self.locomotive}"

    def calculate_wagon_weight(self):
        return sum(wagon.wagon_mass + wagon.load for wagon in self.wagons)

    def check_can_train_move(self, total_wagon_weight: int):
        if self.locomotive.max_towable_mass - self.locomotive.locomotive_mass - total_wagon_weight >= 0:
            return True
        else:
            raise Exception("Train can`t move with this weight")

    @staticmethod
    def sort_trains(train_list: list['Train']) -> list:
        """Sort method of trains, sorts train by train_id"""
        return sorted(train_list, key=lambda d: d.train_id)

    @staticmethod
    def write_to_json(sorted_by_id: list):
        """Method, creates and writes into json file"""
        data = []
        for i in range(len(sorted_by_id)):
            data.append({
                "train_name": sorted_by_id[i].train_name,
                "train_id": sorted_by_id[i].train_id,
                "wagons": [{
                    "wagon_id": x.wagon_id,
                    "load": x.load,
                    "max_mas": x.max_mass,
                    "wagon_mass": x.wagon_mass
                }
                    for x in sorted_by_id[i].wagons],
                "locomotive": [{
                    "id": sorted_by_id[i].locomotive.locomotive_id,
                    "max_towable_mass": sorted_by_id[i].locomotive.max_towable_mass,
                    "locomotive_mass": sorted_by_id[i].locomotive.locomotive_mass
                }],
            })
        json_string = json.dumps(data)
        with open('trains.json', 'w') as outfile:
            outfile.write(json_string)

    # @staticmethod
    # def read_json(json_file: str):
    #     """Method reading json file"""
    #     with open(json_file) as json_file:
    #         data = json.load(json_file)
    #         return data
    # After the program - let’s print out all locomotives
    # with sorted locomotives by their wagons' specific mass sum
    @staticmethod
    def sort_locomotive_by_their_wagon_sum_mass(train_list: list['Train']):
        sorted_train_list = sorted(train_list, key=lambda train: train.calculate_wagon_weight())
        return [train.locomotive for train in sorted_train_list]


class Station:
    def __init__(self, station_name: str, station_location: str, train_capacity: int, train_list: list[Train]):
        self.station_name = station_name
        self.station_location = station_location
        self.train_capacity = train_capacity
        self.train_list = train_list

    def __repr__(self):
        return f"Station name: {self.station_name}, " \
               f"location: {self.station_location}, trains in station: {self.train_list}"

    @staticmethod
    def train_trip(train: Train, station_from: ['Station'], station_to: ['Station']):
        if train in station_from.train_list:
            if len(station_to.train_list) + 1 <= station_to.train_capacity:
                station_from.train_list.remove(train)
                station_to.train_list.append(train)
                return station_to
            else:
                raise Exception("Train station don`t have space for this many trains")
        else:
            raise Exception("Station doesn't have this train")
