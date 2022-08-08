from sortedcontainers import SortedList

def getPaintedAreas(paints):
    events = []
    minDay, maxDay = float('inf'), float('-inf')
    
    for i, se in enumerate(paints):
        events.append((se[0], False, i))
        minDay = min(minDay, se[0])
        events.append((se[1], True, i))
        maxDay = max(maxDay, se[1])

    events = sorted(events)
    
    runningIndices = SortedList()
    eventsIdx = 0
    answer = [0 for _ in range(len(paints))]

    for day in range(minDay, maxDay+1):
        while eventsIdx < len(events) and events[eventsIdx][0] == day:
            eventDay, isEnd, eventIdx = events[eventsIdx]

            if not isEnd:
                runningIndices.add(eventIdx)
            else:
                runningIndices.remove(eventIdx)
            
            eventsIdx += 1

        if runningIndices:
            answer[runningIndices[0]] += 1

    return answer

def main():
    paints = [[1, 4], [4, 7], [5, 8]]
    print(getPaintedAreas(paints))

if __name__ == "__main__":
    main()