import sys
import time
import random


class Stat:
    def __init__(self, list):
        self.list = list

    def sort_half_list(self):
        i = 0
        while i < len(self.list) / 2 + 1:  # stop sort early to save time!
            j = len(self.list) - 2
            while j >= 0:
                # check that the jth value is smaller than j+1th,
                # else swap
                if self.list[j] > self.list[j + 1]:
                    # swap
                    temp = self.list[j]
                    self.list[j] = self.list[j + 1]
                    self.list[j + 1] = temp
                j -= 1
            i += 1
        return self.list

    def median(self):
        return self.list[len(self.sort_half_list())/2]

def generate_experiment(n_numbers, n_times):
    medians = []
    for event_it in range(n_times):
        random_numbers = [random.uniform(0,1) for i in range(n_numbers) ]
        stat = Stat(random_numbers)
        medians.append(stat.median())
    final_stat = Stat(medians)
    print("median of medians %f"%final_stat.median())


if __name__ == "__main__":
    start = time.time()
    generate_experiment(int(sys.argv[1]),int(sys.argv[2]))
    end = time.time()
    print("execution time %f"%(end-start))