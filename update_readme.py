from github import Github

github_username = 'Pvpasall'

g = Github()

user = g.get_user(github_username)

repos = user.get_repos()

with open('README.md', 'a') as f:
    for repo in repos:
        f.write(f"- [{repo.name}]({repo.html_url})\n")
