import unittest

from main import *


class TestTextNode(unittest.TestCase):
    def test_mark(self):
        board = Board()
        board.mark(marker=P1_MARKER, place=(1, 1))
        self.assertEqual(
            board.grid, [["[]", "[]", "[]"], ["[]", "X", "[]"], ["[]", "[]", "[]"]]
        )

        board = Board()
        board.mark(marker=P2_MARKER, place=(1, 1))
        board.mark(marker=P2_MARKER, place=(1, 2))
        board.mark(marker=P2_MARKER, place=(2, 0))
        self.assertEqual(
            board.grid, [["[]", "[]", "[]"], ["[]", "O", "O"], ["O", "[]", "[]"]]
        )

    def test_is_game_end(self):
        # check -
        board = Board()
        board.mark(marker=P1_MARKER, place=(1, 0))
        board.mark(marker=P1_MARKER, place=(1, 1))
        board.mark(marker=P1_MARKER, place=(1, 2))
        self.assertEqual(board.is_game_end(), P1_MARKER)

        # check |
        board = Board()
        board.mark(marker=P1_MARKER, place=(0, 1))
        board.mark(marker=P1_MARKER, place=(1, 1))
        board.mark(marker=P1_MARKER, place=(2, 1))
        self.assertEqual(board.is_game_end(), P1_MARKER)

        # #check \
        board = Board()
        board.mark(marker=P1_MARKER, place=(0, 0))
        board.mark(marker=P1_MARKER, place=(1, 1))
        board.mark(marker=P1_MARKER, place=(2, 2))
        self.assertEqual(board.is_game_end(), P1_MARKER)

        # # check /
        board = Board()
        board.mark(marker=P1_MARKER, place=(0, 2))
        board.mark(marker=P1_MARKER, place=(1, 1))
        board.mark(marker=P1_MARKER, place=(2, 0))
        self.assertEqual(board.is_game_end(), P1_MARKER)

        # # check not ended
        board = Board()
        board.mark(marker=P1_MARKER, place=(0, 2))
        board.mark(marker=P1_MARKER, place=(1, 1))
        board.mark(marker=P1_MARKER, place=(2, 1))
        self.assertEqual(board.is_game_end(), None)


TestTextNode().test_is_game_end()
