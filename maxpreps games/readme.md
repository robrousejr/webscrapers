# Maxpreps Games

**Description:** Accepts [Maxpreps](www.maxpreps.com) URL and scrapes games a team has played in a certain season. Also formats them for a MySQL insertion into a premade database.

## Project Details

* This project was created for a specific database that was already premade
* You can remove `databaseSchoolNumbers` contents (not the list itself) [found here](https://github.com/robrousejr/webscrapers/blob/b48144bb90c7fecebd9af9618b9d6748caa64338/maxpreps%20games/main.py#L19) and change the `outputSQL` function [found here](https://github.com/robrousejr/webscrapers/blob/b48144bb90c7fecebd9af9618b9d6748caa64338/maxpreps%20games/functions.py#L91-L104) if you just want to extract the game information without formatting it into a SQL file

#### User Variables Before Use

[Update These](https://github.com/robrousejr/webscrapers/blob/master/maxpreps%20games/main.py#L15-L22)

## How to Run

* To scrape [Maxpreps](www.maxpreps.com), move into directory and run `py main.py` to get output
* To scrape [MVACBasketball](https://mvacbasketball.com), move into directory and run `py mvac.py` to get output