﻿# GitHub User Activity

A simple Python script to fetch and display the recent public activity of any GitHub user using the GitHub API.

## Features
- Fetches the 10 most recent public events for a specified GitHub user
- Displays event type, repository, and timestamp
- Handles errors and missing users gracefully

## Requirements
- Python 3.6 or higher
- `requests` library

## Installation
1. Clone or download this repository.
2. Install the required Python package:
   ```sh
   pip install requests
   ```

## Usage
Run the script from the command line, providing a GitHub username as an argument:

```sh
python useractivity.py <github-username>
```

**Example:**
```sh
python useractivity.py aidanjames156
```

**Sample Output:**
```
Recent public activity for aidanjames156:
- [2024-06-01T12:34:56Z] PushEvent in aidanjames156/Task-Tracker
- [2024-05-30T09:21:10Z] IssuesEvent in aidanjames156/Portfolio
...
```

If the user has no recent public activity or does not exist, the script will notify you.

## License
MIT License

# Project URL
https://roadmap.sh/projects/github-user-activity
