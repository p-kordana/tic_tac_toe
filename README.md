# Project Name

Tic Tac Toe

## Table of Contents

- [Overview](#overview)
- [Directory Structure](#directory-structure)
- [Installation](#installation)
- [Planning](#planning)

## Overview

Just a simple Python text-based Tic Tac Toe game.

## Directory Structure

### `.gitignore`
Should ignore all Python as well as any Pycharm or VSCode related files.

### `src/`
Source code files.  
singlefile.py is a fully working Tic Tac Toe game in one python file.  
v2/ is a Work in Progress.  

## Installation

All you need is Python.


## Planning

### Basic rules
2 players (Human or 1 Human with AI)  
Player 1 is X  
Player 2 is O  
Players take turns selecting a cell to mark.  
Complete a line (diagonal, vertical, or horizontal) to win  

### Game Loop
Empty game board created  
Player 1 takes turn  
Check for win or draw  
Player 2 takes turn  
Check for win or draw  
Repeat both player turns in order until a win or draw is met  
Print scores  
Ask to replay  
If Y restart loop  
If N exit program  

### TODO
Refactor and comment
Begin work on V2 with multiple classes  
Come up with plan for AI player 