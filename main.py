BOARD_SIZE = 3
EMPTY_MARKER = "[]"
P1_MARKER = "X"
P2_MARKER = "O"
OCUPIED = (P1_MARKER, P2_MARKER)


class Board:
    def __init__(self) -> None:
        self.grid = [[EMPTY_MARKER for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    def mark(self, marker: str, place: tuple[int, int]) -> bool:
        """
        returns True if marked successfully, and False if not
        """
        if place[0] > BOARD_SIZE or place[1] > BOARD_SIZE:
            raise ValueError("there is no such place")
        target_place = self.grid[place[0]][place[1]]
        if target_place in OCUPIED:
            return False
        self.grid[place[0]][place[1]] = marker
        return True

    @staticmethod
    def _check_lines(lines: list) -> str | None:
        for line in lines:
            if EMPTY_MARKER in line:
                continue
            # check for lines
            for marker in OCUPIED:
                match = True
                for space in line:
                    if space == marker:
                        continue
                    else:
                        match = False
                        break
                if match:
                    return marker

    def is_game_end(self) -> str | None:
        """
        returns winning marker or None
        """
        # check for lines
        if result := self._check_lines(self.grid):
            return result
             
        # check for columns
        columns = []
        for i in range(BOARD_SIZE):
            column = []
            for j in range(BOARD_SIZE):
                column.append(self.grid[j][i])
            columns.append(column)
        if result := self._check_lines(columns):
            return result

        # check for cross
        sequence = []
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if i == j:
                    sequence.append(self.grid[i][j])
        if result := self._check_lines([sequence]):
            return result

        sequence = []
        for i in range(BOARD_SIZE):
            j = BOARD_SIZE - 1 - i
            sequence.append(self.grid[i][j])
        if result := self._check_lines([sequence]):
            return result
        return None
