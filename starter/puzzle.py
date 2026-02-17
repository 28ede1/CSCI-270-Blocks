from search import SearchSpace, bfs


class BlockPuzzleSearchSpace(SearchSpace):

    def __init__(self, intervals, cube_width):
        super().__init__()
        self.intervals = intervals
        self.cube_width = cube_width
        self.start_state = ('E', )

    def get_start_state(self):
        """Returns the start state.

        A state of this search space is a sequence of directions. The start state
        contains a single arbitrary initial direction ('E').

        Returns
        -------
        tuple[str]
            The start state
        """
        return self.start_state

    def is_final_state(self, state):
        """Checks whether a given state is a final state.

        To qualify as a final state, the state trajectory should visit all
        positions in a 3x3 cube (without visiting the same position twice).

        Parameters
        ----------
        state : tuple[str]
            A state of the search space, i.e. a sequence of directions

        Returns
        -------
        bool
            True iff the state is a final state
        """
        # Map direction xyz change based on 'E, W, N, S, or U' directions
        position_add_dictionary = {
            'E': (1, 0, 0), 
            'W': (-1, 0 , 0),
            'N': (0, 1, 0),
            'S': (0, -1, 0),
            'U': (0, 0, 1)
        }

        # origin
        curr_pos = (0, 0, 0)

        # To ensure that the same block position in the xyz plane is not visited twice
        position_tracker = [curr_pos]

        # To find the next path coordinate position representation
        for i in range(len(state)):
            curr_pos = tuple(a + b for a, b in zip(curr_pos, position_add_dictionary[state[i]]))

            # You can not be a final state if you have visited the same position twice
            if curr_pos in position_tracker:
                return False
            else:
                position_tracker.append(curr_pos)

        # To ensure that the search path completes a nxnxn cube  
        # ONLY CHECKS FOR A CUBE located in the 1st quadrant
        for x in range(self.cube_width):
            for y in range(self.cube_width):
                for z in range(self.cube_width):
                    if (x, y, z) not in position_tracker:
                        return False
        return True

    def get_successors(self, state):
        """Determines the possible successors of a state.

        A state is a sequence of directions. To generate its successor, we append a direction
        that forces the puzzle to make a 90-degree turn along some axis. In other words,
        one cannot append the direction in which the puzzle is already heading, nor can one
        append the completely opposite direction.

        For instance, if the state is (U, N, W), then we cannot append directions "W" (the
        direction in which the puzzle is currently going) or "E" (the opposite direction)
        to derive a successor.

        Parameters
        ----------
        state : tuple[str]
            A state of the search space, i.e. a sequence of directions

        Returns
        -------
        list[tuple[str]]
            The list of valid successor states.
        """
        raise NotImplementedError("Implement me!")


def construct_search_space_for_2x2x2_puzzle():
    return BlockPuzzleSearchSpace(intervals=(1, 1, 1, 1, 1, 1, 1), cube_width=2)


def construct_search_space_for_3x3x3_puzzle():
    return BlockPuzzleSearchSpace(
        intervals=(2, 2, 2, 2, 1, 1, 1, 2, 2, 1, 1, 2, 1, 2, 1, 1, 2), cube_width=3
    )


def small_solution():
    space = construct_search_space_for_2x2x2_puzzle()
    return bfs(space)


def puzzle_solution():
    space = construct_search_space_for_3x3x3_puzzle()
    return bfs(space)


def solution_b():
    """Computes a solution to block puzzle B from the assignment.

    The solution should be a trajectory, i.e. a sequence of directions
    from the set {'N', 'S', 'E', 'W', 'U', 'D'}. This trajectory should be
    consistent with the shape of the puzzle and should visit each subcube
    of a 3x3 cube exactly once.
    """
    raise NotImplementedError("Implement me!")


def solution_c():
    """Computes a solution to block puzzle C from the assignment.

    The solution should be a trajectory, i.e. a sequence of directions
    from the set {'N', 'S', 'E', 'W', 'U', 'D'}. This trajectory should be
    consistent with the shape of the puzzle and should visit each subcube
    of a 3x3 cube exactly once.
    """
    raise NotImplementedError("Implement me!")
