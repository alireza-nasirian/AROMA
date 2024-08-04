import random
import os

def select_random_packages(repo_path, num_packages=100):
    buildspec_files = []
    for root, dirs, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".buildspec"):
                buildspec_files.append(os.path.relpath(root, file))
    return random.sample(buildspec_files, num_packages)

selected_packages = select_random_packages('content', 100)
with open('selected_packages.txt', 'w') as f:
    for package in selected_packages:
        f.write(f"{package}\n")
