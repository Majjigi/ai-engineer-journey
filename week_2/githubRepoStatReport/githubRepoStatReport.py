import argparse
import json
from pathlib import Path

import requests
from pydantic import BaseModel, ValidationError


class Repository(BaseModel):
	name: str
	stars: int
	language: str | None


def fetch_repositories(username: str) -> list[Repository]:
	repositories = []
	page = 1

	while True:
		response = requests.get(
			f"https://api.github.com/users/{username}/repos",
			params={"per_page": 100, "page": page},
			headers={"Accept": "application/vnd.github+json"},
			timeout=30,
		)
		response.raise_for_status()
		page_data = response.json()
		if not isinstance(page_data, list):
			raise ValueError("GitHub returned an unexpected response format.")

		repositories.extend(
			Repository(
				name=repository["name"],
				stars=repository["stargazers_count"],
				language=repository["language"],
			)
			for repository in page_data
		)

		if len(page_data) < 100:
			return repositories
		page += 1


def main() -> None:
	parser = argparse.ArgumentParser(
		description="Report a GitHub user's public repositories and top five by stars."
	)
	parser.add_argument("username", help="GitHub username to look up")
	args = parser.parse_args()

	try:
		repositories = fetch_repositories(args.username)
	except (requests.RequestException, ValidationError, ValueError, KeyError) as error:
		parser.error(f"Could not fetch or validate repositories: {error}")

	repositories.sort(key=lambda repository: repository.stars, reverse=True)
	report = {
		"username": args.username,
		"repository_count": len(repositories),
		"repositories": [repository.model_dump() for repository in repositories],
	}
	report_path = Path(__file__).with_name("report.json")
	report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

	print(f"GitHub repository report for {args.username}")
	print(f"Public repositories: {len(repositories)}")
	print("Top 5 by stars:")
	if not repositories:
		print("No public repositories found.")
	else:
		for rank, repository in enumerate(repositories[:5], start=1):
			language = repository.language or "Not specified"
			print(f"{rank}. {repository.name} - {repository.stars} stars | {language}")
	print("Full report saved alongside githubRepoStatReport.py as report.json")


if __name__ == "__main__":
	main()
