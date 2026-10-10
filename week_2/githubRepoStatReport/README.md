# GitHub Repository Stats Report

Fetch and validate a user's public GitHub repositories, save the full report to `report.json`, and print the five repositories with the most stars.

## Setup

From this folder, create and activate a virtual environment, then install the dependencies:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run

Pass a GitHub username as the only argument:

```powershell
python .\githubRepoStatReport.py octocat
```

The script requests all public repositories (including forks), validates each repository's name, star count, and language with Pydantic, and writes the full result to `report.json` in this folder.

## Sample output

Example output (repository names and star counts change over time):

```text
GitHub repository report for octocat
Public repositories: 8
Top 5 by stars:
1. Spoon-Knife - 14092 stars | HTML
2. Hello-World - 3805 stars | Not specified
3. octocat.github.io - 1182 stars | CSS
4. hello-worId - 821 stars | Not specified
5. linguist - 768 stars | Ruby
Full report saved alongside githubRepoStatReport.py as report.json
```