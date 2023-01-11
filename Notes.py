Need to solve last attempt to:
    return index before current

while not puzzle.is_goal():
    for item in state_dict.items():
        if (item[0][0], item[0][1]) not in tried_dict.keys():
            add_to_tried(item[0][0], item[0][1])
        print(puzzle.state)
        if len(item[1]) == 0:
            puzzle.set_zero(last_attempt[0], last_attempt[1])
            if len(last_attempt) == 3:
                add_to_tried(last_attempt[0], last_attempt[1], last_attempt[2])
            else:
                add_to_tried(last_attempt[0], last_attempt[1])
            last_attempt = (item[0][0], item[0][1])
            sudoku_solver(puzzle.state)
        elif len(item[1]) == 1:
            if puzzle.is_valid(item[0][0], item[0][1], item[1][0]) and not check_tried((item[0][0], item[0][1]),
                                                                                       item[1][0]):
                puzzle.set_value(item[0][0], item[0][1], item[1][0])
                last_attempt = (item[0][0], item[0][1], item[1][0])
                add_to_tried(item[0][0], item[0][1], item[1][0])
                state_dict = puzzle.get_dict()
            else:
                puzzle.set_zero(last_attempt[0], last_attempt[1])
                state_dict[(item[0][0], item[0][1])] = tuple()
                add_to_tried(item[0][0], item[0][1], item[1][0])
                last_attempt = (item[0][0], item[0][1], item[1][0])
                sudoku_solver(puzzle.state)
        else:
            for val in item[1]:
                if puzzle.is_valid(item[0][0], item[0][1], val) and not check_tried((item[0][0], item[0][1]),
                                                                                    val):
                    puzzle.set_value(item[0][0], item[0][1], val)
                    last_attempt = (item[0][0], item[0][1], val)
                    add_to_tried(item[0][0], item[0][1], item[1][0])
                    state_dict = puzzle.get_dict()
                    break
                else:
                    state_dict[(item[0][0], item[0][1])] = item[1][1:]
                    add_to_tried(item[0][0], item[0][1], val)
                    last_attempt = (item[0][0], item[0][1], val)
            sudoku_solver(puzzle.state)
        print(state_dict)

        current = list(tried_dict.keys()).index(key).

        if len(last_attempt) == 0:
            state_dict.clear()
            state_dict = puzzle.get_dict()
            if len(last_attempt) == 0:
                print(f'Last attempt empty at {key}')
                return np.array([-1] * 81).reshape((9, 9))
            else:
                print(f'Backtracking from {key}')
                sudoku_solver(puzzle.state)


    def get_shortest_value(d):
        if not any(len(x) > 0 for x in d.values()):
            return [k for k in d.keys() if
                    (len(d.get(k)) == min([len(v) for v in d.values()])) and (len(d.get(k)) >= 1)]
        else:
            return [k for k in d.keys() if len(d.get(k)) == min([len(v) for v in d.values()])]


    def get_shortest_value(d):
        if max([len(v) for v in d.values()]) > 0:
            return [k for k in d.keys() if (len(d.get(k)) == min([len(v) for v in d.values()])) > 0]
        else:
            return [k for k in d.keys() if len(d.get(k)) == min([len(v) for v in d.values()])]


    def get_shortest_value(d):
        if max([len(v) for v in d.values()]) > 0:
            mins = {}
            for i, (k, v) in enumerate(d.items()):
                if len(v) > 0:
                    mins.update({k: v})
            print(mins)
            return [k for k in mins.keys() if len(mins.get(k)) == min([len(v) for v in mins.values()])]
        else:
            return [k for k in d.keys() if len(d.get(k)) == min([len(v) for v in d.values()])]