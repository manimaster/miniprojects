import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Initialize the game variables
current_player = 'X'
board = [[' ' for _ in range(3)] for _ in range(3)]

# Function to handle button clicks
def on_button_click(row, col):
    global current_player

    if board[row][col] == ' ':
        buttons[row][col].config(text=current_player)
        board[row][col] = current_player

        if check_win(current_player):
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_game()
        elif check_tie():
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_game()
        else:
            current_player = 'O' if current_player == 'X' else 'X'

# Function to check for a win
def check_win(player):
    for row in range(3):
        if all(board[row][col] == player for col in range(3)):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

# Function to check for a tie
def check_tie():
    return all(cell != ' ' for row in board for cell in row)

# Function to reset the game
def reset_game():
    global current_player, board
    current_player = 'X'
    board = [[' ' for _ in range(3)] for _ in range(3)]
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text=' ')

# Create buttons for the game board
buttons = []
for row in range(3):
    button_row = []
    for col in range(3):
        button = tk.Button(root, text=' ', width=10, height=3, command=lambda r=row, c=col: on_button_click(r, c))
        button.grid(row=row, column=col)
        button_row.append(button)
    buttons.append(button_row)

# Run the application
root.mainloop()
