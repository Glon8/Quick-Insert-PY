# Quick-Insert

**Quick-Insert** is a lightweight Python utility extracted from my old **CustomKeys** project.

It automatically types characters from a selected string through the keyboard as if they were entered by a user. A key trigger can be configured to activate a chat window or another required condition within a game or application. After typing the selected string, Quick-Insert automatically presses **Enter**.

The utility includes double-safe key bindings to prevent accidental activation, as well as a configuration file for additional settings.

## Features

* Types predefined strings through the keyboard
* Configurable key trigger before typing
* Automatically presses **Enter** after typing
* Double-safe key bindings to prevent accidental activation
* Dynamic message selection without restarting the program
* Supports message templates through `templates.json`
* Random message selection mode
* Simple console UI
* Optional emoji-based UI for consoles that support emojis
* Configurable through `config.json`

## Message Templates

The `templates.json` file contains a list of messages that can be selected for insertion.

Messages can be switched using the configured scrolling key bindings, allowing the output to be changed dynamically without closing the program.

### Random Selection

Quick-Insert also includes a random selection mode.

When `random_selection` is enabled, manual scrolling is disabled. Instead, Quick-Insert randomly selects a message from the available templates whenever the insertion is triggered.

## Requirements

* Python **3.12.6 or higher** when activating the program through a code editor
* `pynput`
* `rich`

Install the required packages with:

```bash
pip install pynput rich
```

## Usage

1. Download the project files.
2. Build the program with **PyInstaller**.
3. Run the program for the first time. `config.json` and `templates.json` will be created.
4. Make sure the **kill switch is off**.
5. Open `config.json` and `templates.json` and configure them according to your needs.
6. Activate the kill switch when you are ready to use the program.

## `config.json` Guide

### `display`

Controls whether the console interface uses emojis or plain text.

### `key_[...]`

Configures the keyboard bindings used by the program.

It is recommended to use at least two keys together for important triggers to prevent accidental activation.

> **Note:** Special keys are not supported.

### `random_selection`

Controls random message selection.

* `0` – Disabled (default)
* `1` – Enabled

When enabled, Quick-Insert randomly selects a message from `templates.json` instead of allowing the user to manually scroll through the available messages.

### `.[min/max]_delay`

Sets the minimum and maximum delay between individual key presses.

The values are specified in **milliseconds**.

For example:

```text
min_delay = 100
max_delay = 500
```

The delay is randomized between the configured limits.

> **Warning:** Setting the delay too low may result in input being detected as unnatural by some applications or anti-cheat systems.

### `.max_disturbance`

Sets the maximum limit of disturbance between individual key presses.

The values are specified in **milliseconds**.

## `templates.json` Guide

Add your messages to the template list.

For example:

```json
[
    "Hello! I'm David!"
]
```

Multiple messages can be added:

```json
[
    "Hello! I'm David!",
    "Your message",
    "Another message"
]
```

The configured scrolling keys can then be used to switch between these messages, unless `random_selection` is enabled.

## Project Status

**Finished**
