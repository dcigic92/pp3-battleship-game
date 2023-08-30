# Battleship Game

**Battleship Game is a Python terminal game which runs on Heroku. Users are supposed to beat the computer by sinking all of the computer's battleships before computer sinks theirs. Each battleship occupies one field on the grid.**

***[Live version](https://dcigic92-pp3-battleship-game-e0f029a41560.herokuapp.com/)*** created by **Dino Cigic**.

## Technologies Used
- Python
- [Heroku](https://heroku.com/)
- [Git](https://git-scm.com/)
- [Github](https://github.com/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [W3Schools](https://www.w3schools.com/)
- [Stack Overflow](https://stackoverflow.com/)
- [CI Python Linter](https://pep8ci.herokuapp.com/)

## Testing

### Manual testing
Tested by playing a lot of times looking for bugs and by intentionally giving invalid inputs.

### PEP8 Python Validator
The PEP8 Python Validator (CI Python Linter) was used to validate all Python files. All files passed with no errors.

### Bugs
- Had bug where it was possible to attack more than once on the same coordinates. Fixed it with while loop, if there is no ship on given coordinates and it's not empty field, it will loop again.

- Had bug where it was possible to put more ships on the same coordinates. Fixed it with while loop, if on given coordinates is not empty field it will loop again.

## Deployment

This project was deployed on Heroku.

- Steps for deployment:
    - Create a new Heroku app.
    - In Heroku's settings add config var (key PORT, value 8000).
    - Set the buildbacks to Python and NodeJS in that order.
    - Link the Heroku app to the Github repository.
    - Click on deploy.

## Credits

### Code

- A lot of python code learned on [W3Schools](https://www.w3schools.com/) and [Stack Overflow](https://stackoverflow.com/).
- ASCII art title taken from [patorjk](https://patorjk.com/software/taag/#p=display&f=Stforek&t=BATTLESHIP%20GAME).

## Acknowledgements

- My mentor **Akshat Garg** for his feedback and advice.
- Our cohort facilitator **Alan Bushell** and slack community.