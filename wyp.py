main = input().split()
n = int(main[0])
D = int(main[1])
W = int(main[2])
M = int(main[3])

traffic = []

class Vehicle:
    def __init__(self, x, d, w, m):
        self.start = float(x)
        self.end = float(x)-float(d)
        self.speed = float(w)/float(m)


class Event:
    def __init__(self, time, a, b):
        self.time = time
        self.objects = [a, b]

    def occur(self, last_time):
        update_positions(last_time, self.time)
        self.objects[0].speed = self.objects[1].speed
        recount_events(events, self.time)
        events.sort(key=lambda x: x.time)


events = []
overtake_timepoints = []
next_overtakes = []

def count(vehicleA, vehicleB):
    distance = vehicleB.end - vehicleA.start
    speed = vehicleA.speed - vehicleB.speed
    timepoint = distance / speed
    events.append(Event(timepoint, vehicleA, vehicleB))

def recount_events(events, time):
    for i in events:
        if i.objects[1].end != i.objects[0].start and i.objects[1].speed != i.objects[0].speed:
            i.time = time + (i.objects[1].end-i.objects[0].start) / (i.objects[0].speed-i.objects[1].speed)
        else:
            i.time = time

def update_positions(last_time, current_time):
    for i in traffic:
        i.start += (current_time - last_time) * i.speed
        i.end += (current_time - last_time) * i.speed
    main_character.start = current_time * main_character.speed
    main_character.end = current_time * main_character.speed

def compute_overtakes(current_time, overtake_timepoints, next_overtakes):
    for i in range(0, len(traffic)):
        if traffic[i].end >= main_character.start:
            distance = traffic[i].end - main_character.start
            time_needed_to_overtake = current_time + (distance / (main_character.speed - traffic[i].speed))
            overtake_timepoints.append(time_needed_to_overtake)
            next_overtakes.append(i)

main_character = Vehicle(0, D, W, M)

for i in range(n):
    info = input().split()
    traffic.append(Vehicle(info[0], info[1], info[2], info[3]))

for i in range(len(traffic)-2, -1, -1):
    if traffic[i].speed>traffic[i+1].speed:
        count(traffic[i], traffic[i+1])

events.sort(key=lambda x: x.time)

fin = 0
current_time = 0

compute_overtakes(current_time, overtake_timepoints, next_overtakes)

# print(*overtake_timepoints, sep=", ")
# print(*next_overtakes, sep=", ")
# for i in events:
#     print(i.time)

i = 0
while True:
    try:
        if overtake_timepoints[i]<=events[0].time:
            if i>0:
                update_positions(current_time, overtake_timepoints[i])
                current_time = overtake_timepoints[i]
                if traffic[next_overtakes[i]].end - traffic[next_overtakes[i]-1].start >= D:
                    fin += 1
            else:
                update_positions(current_time, overtake_timepoints[i])
                current_time = overtake_timepoints[i]
                fin += 1
            i += 1
        else:
            events[0].occur(current_time)
            current_time = events[0].time
            events.remove(events[0])
            overtake_timepoints = []
            next_overtakes = []
            compute_overtakes(current_time, overtake_timepoints, next_overtakes)
            i = 0
    except IndexError:
        if i > len(overtake_timepoints)-1:
            break
        if next_overtakes[i] > 0:
            update_positions(current_time, overtake_timepoints[i])
            current_time = overtake_timepoints[i]
            if traffic[next_overtakes[i]].end - traffic[next_overtakes[i] - 1].start >= D:
                fin += 1
        else:
            update_positions(current_time, overtake_timepoints[i])
            current_time = overtake_timepoints[i]
            fin += 1

        i += 1


print(fin)