# SoberLife II

A Pygame based board game where you try to make it through the day without getting too stressed! 

Written by Bruce Baskir.

- [SoberLife II](#soberlife-ii)
- [Instructions](#instructions)
- [Installation](#installation)
  - [Windows](#windows)
    - [Install Python](#install-python)
    - [Install Game](#install-game)
- [Building](#building)
  - [Windows](#windows-1)

# Instructions

You are trying to make it through the day without getting too stressed.

Click the space on the activity on which you wish to start.

Each turn you move by clicking on a space adjacent to your present space.

Some activities are stressful, others are calming.

Delaying a stressful activity will make it more stressful.

Clusters of stressful activities become more stressful more quickly.

You win by making it through until 8:00pm.

You lose if your stress level becomes too high or if any activity attains a stress level greater than five.

Good luck!!!


# Installation
The following commands should be executed from the same folder in which this README file can be found (unless noted otherwise). Shell commands have been written for the [powershell cli](https://en.wikipedia.org/wiki/PowerShell).

## Windows

### Install Python
Python can be installed from [python.org](https://www.python.org/downloads/) or using the [Chocolatey](https://chocolatey.org/) package manager. **This will need to sync up with the version of [pygame](https://www.pygame.org) that you plan on using!**. The follwoing instructions all assume that [python3 is on your PATH](https://www.pygame.org/wiki/GettingStarted#Windows%20installation).

If you have [Chocolatey](https://chocolatey.org) installed, you can use the [following command to install Python](https://chocolatey.org/packages/python/).

```powershell
# Install python 3.6.7
choco install python --version 3.6.7
```

### Install Game
Dependencies can be manually installed or installed automatically via pip and the [requirements.txt](requirements.txt) file. If this fails, follow the manual install instructions found on [pygame's wiki](https://www.pygame.org/wiki/GettingStarted#Windows%20installation)

```powershell
# Install game
pip install .
```

You should now have all the dependencies downloaded locally and can run the executable file from the command line.

```powershell
# Start game via CLI
& 'SoberLife II.exe'
```

You can also invoke the entry point using python.

```powershell
python '.\SoberLife II.py'
```

# Building
## Windows
To create a standalone .exe file (has python and dependencies bundled), first download and [Install Python](#install-python), then install [pyinstaller](https://pyinstaller.readthedocs.io/en/stable/installation.html). 

```powershell
# install pyinstaller
pip install pyinstaller

# Build .exe file in ./dist folder
pyinstaller 'SoberLife II.spec'

# Run .exe from command line
& '.\dist\SoberLife II.exe'
```

'.\dist\SoberLife II.exe' can now be distributed without the need for the end users to install python or any dependencies. 
