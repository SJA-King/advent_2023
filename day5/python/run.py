import os
from functools import lru_cache

HERE = os.path.dirname(os.path.abspath(__file__))
EXAMPLE = os.path.join(HERE, "../example.txt")
EXAMPLE2 = os.path.join(HERE, "../example2.txt")
INPUT = os.path.join(HERE, "../input.txt")


def get_data(the_file: str):
    data = []
    with open(the_file, 'r') as it:
        for line in it.readlines():
            data.append(line.strip())

    return data


from dataclasses import dataclass, field


@dataclass
class Range:
    start: int = 0
    stop: int = 9999


@dataclass
class Map:
    name: str = ""
    source_start: list[int] = field(default_factory=list)
    destination_start: list[int] = field(default_factory=list)
    amount: list[int] = field(default_factory=list)
    source_list: list[Range] = field(default_factory=list)
    destination_list: list[Range] = field(default_factory=list)

    # def __post_init__(self):
    #     self.create_range_lists()

    def create_range_lists(self):
        self.source_list = []
        self.destination_list = []
        for src_idx, i_src in enumerate(self.source_start):
            self.source_list.append(
                Range(
                    start=i_src,
                    stop=i_src + self.amount[src_idx]))
            self.destination_list.append(
                Range(
                    start=self.destination_start[src_idx],
                    stop=self.destination_start[src_idx] + self.amount[src_idx]))

    @lru_cache
    def convert(self, a_number: int) -> int:
        a_number = int(a_number)
        result = None
        for src_idx, src_range in enumerate(self.source_list):
            if src_range.start <= a_number <= src_range.stop:
                src_difference = a_number - src_range.start
                result = self.destination_list[src_idx].start + src_difference
                break

        if not result:
            # if not mapped return it as is
            result = a_number

        print(f"Map ({self.name}) mapped '{a_number}' -> '{result}'!")
        return result


def part_1(the_data):
    print("Part 1")

    key_ss = "seed-to-soil"
    key_sf = "soil-to-fertilizer"
    key_fw = "fertilizer-to-water"
    key_wl = "water-to-light"
    key_lt = "light-to-temperature"
    key_th = "temperature-to-humidity"
    key_hl = "humidity-to-location"

    keys_to_maps = {
        key_ss: Map(name=key_ss),
        key_sf: Map(name=key_sf),
        key_fw: Map(name=key_fw),
        key_wl: Map(name=key_wl),
        key_lt: Map(name=key_lt),
        key_th: Map(name=key_th),
        key_hl: Map(name=key_hl),
    }

    seeds = []
    the_map = None

    for line in the_data:

        if "seeds:" in line:
            # e.g. seeds: 79 14 55 13
            seeds = list(filter(None, line.split(" ")))
            seeds.remove("seeds:")
            print(f"Seeds! = {seeds}")
            continue

        if len(line) == 0:
            the_map = None
        if the_map:
            line_run = list(filter(None, line.split(" ")))
            print(f"Map has -> {line_run}")
            the_map.destination_start.append(int(line_run[0]))
            the_map.source_start.append(int(line_run[1]))
            the_map.amount.append(int(line_run[2]))

        if not the_map:
            for key, key_map in keys_to_maps.items():
                if key in line:
                    the_map = key_map
                    break

    for a_map in keys_to_maps.values():
        a_map.create_range_lists()

    lowest_location = 9999999999999999999999999999
    for a_seed in seeds:

        a_soil = keys_to_maps[key_ss].convert(a_seed)
        a_fert = keys_to_maps[key_sf].convert(a_soil)
        a_water = keys_to_maps[key_fw].convert(a_fert)
        a_light = keys_to_maps[key_wl].convert(a_water)
        a_temperature = keys_to_maps[key_lt].convert(a_light)
        a_humidity = keys_to_maps[key_th].convert(a_temperature)
        a_location = keys_to_maps[key_hl].convert(a_humidity)

        if a_location < lowest_location:
            lowest_location = a_location

    return lowest_location
    # my answer = 525792406


def part_2(the_data):
    print("Part 2")

    key_ss = "seed-to-soil"
    key_sf = "soil-to-fertilizer"
    key_fw = "fertilizer-to-water"
    key_wl = "water-to-light"
    key_lt = "light-to-temperature"
    key_th = "temperature-to-humidity"
    key_hl = "humidity-to-location"

    keys_to_maps = {
        key_ss: Map(name=key_ss),
        key_sf: Map(name=key_sf),
        key_fw: Map(name=key_fw),
        key_wl: Map(name=key_wl),
        key_lt: Map(name=key_lt),
        key_th: Map(name=key_th),
        key_hl: Map(name=key_hl),
    }

    seed_ranges = []
    the_map = None

    for line in the_data:

        if "seeds:" in line:
            # e.g. seeds: 79 14 55 13
            seed_ranges = list(filter(None, line.split(" ")))
            seed_ranges.remove("seeds:")
            print(f"Seed Ranges! = {seed_ranges}")
            continue

        if len(line) == 0:
            the_map = None
        if the_map:
            line_run = list(filter(None, line.split(" ")))
            print(f"Map has -> {line_run}")
            the_map.destination_start.append(int(line_run[0]))
            the_map.source_start.append(int(line_run[1]))
            the_map.amount.append(int(line_run[2]))

        if not the_map:
            for key, key_map in keys_to_maps.items():
                if key in line:
                    the_map = key_map
                    break

    for a_map in keys_to_maps.values():
        a_map.create_range_lists()

    lowest_location = 9999999999999999999999999999
    for i in range(len(seed_ranges)):
        if i % 2 != 0:
            pass
        else:
            for a_seed in list(range(int(seed_ranges[i]), int(seed_ranges[i]) + int(seed_ranges[i + 1]))):
                print(f"A Seed is {a_seed}")
                a_soil = keys_to_maps[key_ss].convert(a_seed)
                a_fert = keys_to_maps[key_sf].convert(a_soil)
                a_water = keys_to_maps[key_fw].convert(a_fert)
                a_light = keys_to_maps[key_wl].convert(a_water)
                a_temperature = keys_to_maps[key_lt].convert(a_light)
                a_humidity = keys_to_maps[key_th].convert(a_temperature)
                a_location = keys_to_maps[key_hl].convert(a_humidity)

                if a_location < lowest_location:
                    print(f"New lowest Location = {lowest_location}")
                    lowest_location = a_location

    return lowest_location



def main():
    print("Day 5")

    # example_data = get_data(EXAMPLE)
    # result = part_1(example_data)
    # print(result)
    # #
    # input_data = get_data(INPUT)
    # result = part_1(input_data)
    # print(result)

    # example_2_data = get_data(EXAMPLE)
    # result = part_2(example_2_data)
    # print(result)
    #
    input_data = get_data(INPUT)
    result = part_2(input_data)
    print(result)


if __name__ == "__main__":
    main()