# CodePet

A gamified task tracker with an evolving pixel pet companion. Stay motivated to complete your tasks by nurturing your virtual pet!

## Features

- **Task Management**: Create, complete, and organize tasks with subtask support
- **XP System**: Earn experience points by completing tasks
- **Leveling**: Level up your pet as you accumulate XP
- **Pet Evolution**: Watch your pet evolve through 5 stages (egg, baby, child, teen, adult)
- **Visual Feedback**: Celebratory notifications for level-ups and evolutions
- **Persistent Storage**: Your progress is saved locally using SQLite

## Screenshots

*Coming soon*

## Installation

### Prerequisites

- Python 3.8 or higher

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/J-Lehrer/CodePet.git
   cd CodePet
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv

   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application:

```bash
python main.py
```

### How to Play

1. **Add Tasks**: Click the "+ Add Task" button to create a new task
2. **Complete Tasks**: Click the circle (○) next to a task to mark it complete and earn XP
3. **Add Subtasks**: Click the "+" button on any task to add subtasks (worth partial XP)
4. **Watch Your Pet Grow**: As you earn XP, your pet will level up and evolve!

### Evolution Stages

| Stage | Level Required |
|-------|---------------|
| Egg   | 1 (starting)  |
| Baby  | 2             |
| Child | 5             |
| Teen  | 10            |
| Adult | 20            |

## Project Structure

```
CodePet/
├── main.py          # Main application and UI
├── database.py      # SQLite database management
├── requirements.txt # Python dependencies
├── LICENSE          # MIT License
└── README.md        # This file
```

## Dependencies

- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) - Modern UI framework
- [Pillow](https://python-pillow.org/) - Image processing
- [platformdirs](https://github.com/platformdirs/platformdirs) - Cross-platform data directories

## Data Storage

Your data is stored locally in your user data directory:
- **Windows**: `%LOCALAPPDATA%\CodePet\CodePet\codepet.db`
- **macOS**: `~/Library/Application Support/CodePet/codepet.db`
- **Linux**: `~/.local/share/CodePet/codepet.db`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
