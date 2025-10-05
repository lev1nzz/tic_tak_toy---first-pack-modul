# Объявить класс.
class Board:
    """Класс, который описывает игровое поле."""
    # Новый атрибут.
    field_size = 3
    
    def __init__(self):
        self.board = [
            [' ' for _ in range(self.field_size)] for _ in range(self.field_size)
        ]
        
    # Метод, который отрабатывет ходы игроков.
    def make_move(self, row, col, player):
        self.board[row][col] = player
        
    # Метод, который отрисовывает игровое поле.
    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)
    
    def __str__(self):
        return (
            'Объект игрового поля размером '
            f'{self.field_size}x{self.field_size}'
        ) 