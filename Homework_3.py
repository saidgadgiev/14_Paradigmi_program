"""ДЗ № 3  Игра крестики-нолики"""
class TicTacToeGame:
    def __init__(self):
        self.board = [' '] * 9
        self.current_player = 'X'

    def print_board(self):
        for i in range(0, 9, 3):
            print(self.board[i], '|', self.board[i+1], '|', self.board[i+2])
            if i < 6:
                print('-' * 9)

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print('Неверный ход. Попробуйте еще раз.')

    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # горизонтальные линии
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # вертикальные линии
            [0, 4, 8], [2, 4, 6]              # диагонали
        ]

        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return self.board[combo[0]]

        if ' ' not in self.board:
            return 'Ничья'

        return None

    def play(self):
        while True:
            self.print_board()
            print(f'Ход игрока {self.current_player}')

            try:
                position = int(input('Выберите позицию (от 1 до 9): ')) - 1
                if position < 0 or position > 8:
                    raise ValueError
            except ValueError:
                print('Неверная позиция. Попробуйте еще раз.')
                continue

            self.make_move(position)
            winner = self.check_winner()

            if winner:
                self.print_board()
                if winner == 'Ничья':
                    print('Ничья!')
                else:
                    print(f'Игрок {winner} выиграл!')
                break


game = TicTacToeGame()
game.play()
