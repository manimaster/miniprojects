# Problem with AI logic. Has to fix :)

import tkinter as tk
from tkinter import messagebox
import random

# Create the main application window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Initialize the game variables
player = 'X'
computer = 'O'
board = [[' ' for _ in range(3)] for _ in range(3)]

# Function to handle button clicks
def on_button_click(row, col):
    global player
    if board[row][col] == ' ':
        buttons[row][col].config(text=player)
        board[row][col] = player

        if check_win(player):
            messagebox.showinfo("Game Over", f"Player {player} wins!")
            reset_game()
        elif check_tie():
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_game()
        else:
            player = 'X' if player == 'O' else 'O'
            if player == 'O':
                computer_move()

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
    global player, board
    player = 'X'
    board = [[' ' for _ in range(3)] for _ in range(3)]
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text=' ')

# Function to make the computer move using minimax algorithm
def computer_move():
    best_score = float('-inf')
    best_move = None

    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = computer
                score = minimax(board, 0, False)
                board[row][col] = ' '

                if score > best_score:
                    best_score = score
                    best_move = (row, col)

    if best_move:
        row, col = best_move
        buttons[row][col].config(text=computer)
        board[row][col] = computer

        if check_win(computer):
            messagebox.showinfo("Game Over", "Computer wins!")
            reset_game()
        elif check_tie():
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_game()
        else:
            player = 'X'

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    if check_win(computer):
        return 1
    elif check_win(player):
        return -1
    elif check_tie():
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = computer
                    score = minimax(board, depth + 1, False)
                    board[row][col] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = player
                    score = minimax(board, depth + 1, True)
                    board[row][col] = ' '
                    best_score = min(score, best_score)
        return best_score

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
