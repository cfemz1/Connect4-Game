# Connect 4 Game – Python

A group-developed Connect 4 application created for the **CMP5368 Applied Programming** module at Birmingham City University.

The project provides a console interface and a Tkinter graphical interface. It demonstrates Python programming, object-oriented design, game-state management, computer-player logic, file persistence and functional testing.

## Technologies
- Python 3
- Tkinter (Python GUI toolkit)
- JSON (saving and loading game state)
- Object-oriented programming

## Features represented in the submitted source
- Configurable board dimensions (default 6 × 7)
- Console and Tkinter graphical interfaces
- Human vs Human, Human vs Computer and Computer vs Computer modes
- Player symbols and colour selection in the GUI
- Gravity-based piece placement and full-column handling
- Horizontal, vertical and diagonal win detection
- Draw detection
- Computer moves: random selection and a strategic mode that checks immediate winning and blocking moves, then prefers the centre column
- Save/load of board state using JSON
- Animated disc movement in the graphical interface

## Project structure
| File | Purpose |
|---|---|
| `connect4.py` | Application entry point and console game orchestration |
| `gameboard.py` | Board state, piece placement, win/draw checks and JSON persistence |
| `player.py` | Player classes, human input and computer move selection |
| `gamegui.py` | Tkinter interface, interaction, animation and GUI game flow |
| `Connect4_Test_Plan.docx` | Submitted functional test plan |
| `Connect4_Program_Design.pptx` | Submitted design documentation and architecture |

## How to run
1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python connect4.py
```

Tkinter is included with many standard Python installations. On some Linux distributions it may need to be installed separately.

## Design
The program design document describes an MVC-inspired layered structure:
- **Model:** `GameBoard`
- **View:** `GameGUI`
- **Controller:** `connect4.py`
- **Player layer:** `Player`, `HumanPlayer` and `ComputerPlayer`

The board is represented as a two-dimensional list. Save files use JSON to store board dimensions and the current board state.

## Testing
The submitted test plan records **20 manually executed functional test cases, all marked as passed**. Coverage includes symbol selection, input validation, gravity/piece placement, full-column handling, horizontal/vertical/diagonal wins, draw detection, computer-player behaviour and game modes.

See `Connect4_Test_Plan.docx` for the detailed cases and results.

## Scope and implementation notes
This repository contains the supplied project files and documentation. The design presentation describes a hard AI using minimax with alpha-beta pruning, but the supplied `player.py` implements easy random play and a strategic mode that checks immediate wins/blocks and centre preference. The hard minimax algorithm is not present in the supplied source files, so it is not claimed as implemented here.

The design documentation also discusses save/load in the console flow; the supplied GUI includes save/load controls. The supplied console and GUI files are preserved as submitted rather than silently rewritten. As with many coursework projects, review and test the code in your own Python environment before relying on it as a standalone release.


