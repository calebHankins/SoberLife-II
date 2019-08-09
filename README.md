# SoberLife II

- [SoberLife II](#soberlife-ii)
- [Installation](#installation)
  - [Windows](#windows)
    - [Install Python](#install-python)
  - [Install Project Dependencies](#install-project-dependencies)
- [Instructions](#instructions)
  - [Start Game](#start-game)

# Installation
The following commands should be executed from the same folder in which this README file can be found (unless noted otherwise).

## Windows

### Install Python
Python can be installed from [python.org](https://www.python.org/downloads/) or using the [Chocolatey](https://chocolatey.org/) package manager. **This will need to sync up with the version of [pygame](https://www.pygame.org) that you plan on using!**

If you have [Chocolatey](https://chocolatey.org) installed, you can use the [following command to install Python](https://chocolatey.org/packages/python/).

```powershell
# Install python 3.6.7
choco install python --version 3.6.7
```

## Install Project Dependencies
Dependencies can be manually installed or installed automatically via pip and the [requirements.txt](requirements.txt) file. If this fails, follow the manual install instructions found on [pygame's wiki](https://www.pygame.org/wiki/GettingStarted#Windows%20installation)

```powershell
# Install project dependencies
pip install --user -r requirements.txt
```

# Instructions

## Start Game

```powershell
# Start game
python '.\SoberLife II.py'
```