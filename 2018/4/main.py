with open("./in.txt") as f:
    content = [line.rstrip('\n') for line in f]

def main():
    # print(sorted(content))
    guards = {}
    guard = None
    asleep_min = 0
    for c in sorted(content):
        minute = int(c[15:17])
        action = c.split(" ")[2]
        if action == "Guard":
            guard = int(c.split(" ")[3][1:])
            if not guards.get(guard):
                guards[guard] = [0 for x in range(60)]
        elif action == "wakes":
            print(asleep_min, minute)
            for x in range(asleep_min, minute+1):
                guards[guard][x] += 1
            assert asleep_min < minute
        elif action == "falls":
            asleep_min = minute
    print(guards)
    sleeeps = -1
    sleepiest = -1
    # for num, sleeps in guards.items():
    #     if sleeeps < sum(sleeps):
    #         sleeeps = sum(sleeps)
    #         sleepiest = num
    # print(sleepiest, guards[sleepiest])
    # print(guards[sleepiest].index(max(guards[sleepiest])))
    # print(guards[sleepiest].index(max(guards[sleepiest])) * sleepiest)

    for num, sleeps in guards.items():
        if sleeeps < max(sleeps):
            sleeeps = max(sleeps)
            sleepiest = num
    print(sleepiest, guards[sleepiest])
    print(guards[sleepiest].index(max(guards[sleepiest])))
    print(guards[sleepiest].index(max(guards[sleepiest])) * sleepiest)
main()
