import random

BOARD_SIZE = 3
EMPTY_MARKER = " "
P1_MARKER = "X"
P2_MARKER = "O"
OCUPIED = (P1_MARKER, P2_MARKER)


class Player:
    marker: str
    name: str

    def __init__(self, name: str, marker: str) -> None:
        if marker == EMPTY_MARKER:
            raise ValueError("This is reserved")
        self.marker = marker
        self.name = name

    def hit(self) -> tuple[int, int]:
        raise NotImplementedError()


class BotPlayer(Player):
    def __init__(self, name: str, marker: str) -> None:
        super().__init__(name, marker)

    def hit(self) -> tuple[int, int]:
        return random.randint(0, BOARD_SIZE -1), random.randint(0, BOARD_SIZE - 1)


class HumanPlayer(Player):
    def __init__(self, marker: str) -> None:
        name = input("Enter your name: ")
        super().__init__(name, marker)

    def _get_coordinate_usr_input(self, input_name: str) -> int:
        while True:
            result = input(f"{self.name}, please enter {input_name} coordinate: ")
            try:
                result = int(result)
            except ValueError:
                print(f"{input_name} must be an int, received {type(result)}")
                continue
            if result > BOARD_SIZE:
                print(f"{input_name} is too big")
            elif result < 0:
                print(f"{input_name} can't be a negative number")
            else:
                break
        return result

    def hit(self) -> tuple[int, int]:
        return self._get_coordinate_usr_input("y"), self._get_coordinate_usr_input("x")

class Board:
    def __init__(self) -> None:
        self.grid = [[EMPTY_MARKER for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    def mark(self, marker: str, place: tuple[int, int]) -> bool:
        """
        returns True if marked successfully, and False if not
        """
        if place[0] > BOARD_SIZE or place[1] > BOARD_SIZE:
            return False
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

    def draw_grid(self) -> str:
        result = "---" * BOARD_SIZE
        result += "\n"
        for line in self.grid:
            result += " | ".join(line) + "\n"
            result += "---" * BOARD_SIZE
            result += "\n"
        return result

def update_screen(screen: str):
    print("\033[2J\033[H", end="")
    print(screen)


class Game():
    board: Board
    players: list[Player]

    def __init__(self) -> None:
        self.board = Board()
        p1 = HumanPlayer(marker=P1_MARKER)
        p2 = BotPlayer("bot", P2_MARKER)
        self.players = [p1, p2]

    def start_game_loop(self):
        while True:
            update_screen(self.board.draw_grid())
            for player in self.players:
                while True:
                    place = player.hit()
                    if not self.board.mark(player.marker, place):
                        print("choose another spot")
                        continue
                    else:
                        break
                update_screen(self.board.draw_grid())
                if result := self.board.is_game_end():
                    print(f"{result} wins!")
                    return


if __name__ == "__main__":
    game = Game()
    game.start_game_loop()
