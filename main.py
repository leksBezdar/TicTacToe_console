from enum import Enum


class PlayerSymbols(Enum):
    X = "X"
    O = "O"


class Board:
    def __init__(self) -> None:
        self.board: list[list] = [[" " for _ in range(3)] for _ in range(3)]

    def draw_board(self):
        for row in self.board:
            print(" | ".join(row))
            print("-" * 9)


class GameStateManager:

    def __init__(self, board: Board) -> None:
        self.board: list[list] = board.board

    def check_winner(self, row, col) -> bool:

        # Горизонталь
        if self.board[row].count(self.board[row][col]) == len(self.board[row]) and self.board[row][col] != " ":
            return True

        # Вертикаль
        if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != " ":
            return True

        # Диагонали
        if row == col and self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != " ":
            return True

        if row + col == 2 and self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != " ":
            return True

        return False

    def check_draw(self):
        return all(self.board[i][j] != " " for i in range(3) for j in range(3))


class Player:
    def __init__(self, symbol) -> None:
        self.symbol = symbol


class Move:
    def __init__(self, board: Board) -> None:
        self.board: list[list] = board.board

    def check_move(self, row, col) -> bool:
        return self.board[row - 1][col - 1] == " "

    def make_move(self, player, row, col) -> bool:
        if self.check_move(row, col):
            self.board[row - 1][col - 1] = player
            return True
        else:
            print("Слот уже занят!")
            return False


class TicTacToeGame:
    def __init__(self) -> None:
        self.board = Board()
        self.move = Move(self.board)
        self.game_state_manager = GameStateManager(self.board)
        self.players = [Player(PlayerSymbols.X), Player(PlayerSymbols.O)]
        self.turn = 0

    def play(self):
        while True:
            self.board.draw_board()
            current_player = self.players[self.turn % 2].symbol.value
            row, col = map(int, input(
                f"Игрок {current_player}, введите координаты хода в формате 'строка,столбец': ").split(','))

            if self.move.make_move(current_player, row, col):
                if self.game_state_manager.check_winner(row - 1, col - 1):
                    self.board.draw_board()
                    print(f"Игрок {current_player} победил!")
                    break
                elif self.game_state_manager.check_draw():
                    self.board.draw_board()
                    print("Ничья!")
                    break

                self.turn += 1


if __name__ == "__main__":
    tic_tac_toe = TicTacToeGame()
    tic_tac_toe.play()
