# Loading Screen Improvements

## Overview

This document describes the custom loading screen implementation for the SoberLife-II web version using pygbag.

## Problem

When running the game via pygbag in a web browser, there can be a noticeable delay before the user can interact with the game. During this time, users might think the application is broken or frozen, leading to a poor user experience.

## Solution

We've created a custom pygbag template (`custom.tmpl`) that displays user-friendly loading messages during different stages of the initialization process:

### Loading Stages

1. **"Loading SoberLife-II..."** - Displayed while downloading and mounting the game files
2. **"Preparing game assets..."** - Shown while preloading images and compiling WASM modules
3. **"Setting up [package]..."** - Appears when setting up specific packages
4. **"Ready to start!"** - Final message before the game begins, with a "Click or tap to begin" prompt

### Visual Features

- **Progress Bar**: A green progress bar shows the download/loading progress
- **Consistent Styling**: Loading messages use the same color scheme as the game (teal/cyan: RGB 100, 200, 200)
- **Clear Positioning**: Messages are positioned above the progress bar for easy visibility
- **Responsive Design**: The template uses relative positioning that adapts to different screen sizes

## Usage

To use the custom loading screen, run pygbag with the `--template` flag:

```bash
# For local development
pygbag --template custom.tmpl .

# For building deployment files
pygbag --build --template custom.tmpl .
```

## Technical Details

The custom template is based on pygbag's default template but includes:

- Custom `fnt_loading` font for loading messages
- Screen clearing (`screen.fill`) before each message update to prevent visual artifacts
- Consistent message rendering during all loading phases
- Enhanced user engagement prompt with clearer instructions

## Files Modified

- **`custom.tmpl`** - Custom pygbag template with loading messages
- **`README.md`** - Updated to include instructions for using the custom template

## Future Improvements

Potential enhancements could include:

- Animated loading indicators (spinner, dots, etc.)
- Percentage-based progress display
- Estimated time remaining
- Custom loading graphics/logo
- Fade-in/fade-out transitions between loading stages
