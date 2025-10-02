#!/usr/bin/env python3
"""
Test script to verify command line argument parsing
"""
import click
import os

@click.command()
@click.argument('project_directory',
                type=click.Path(exists=True, file_okay=False, dir_okay=True))
@click.option('--task', '-t', help='Task to execute')
def main(project_directory, task=None):
    project_dir = os.path.abspath(project_directory)
    print(f"Project directory: {project_dir}")
    
    # If no task provided via option, check if directory name suggests a task
    if task is None:
        dir_name = os.path.basename(project_dir)
        print(f"No task provided, directory name is: {dir_name}")
        # If the directory name looks like a common task, use it
        if dir_name in ['snake', 'game', 'demo']:
            task = f"Create a {dir_name} game using HTML, CSS, and JavaScript in the current directory."
            print(f"Inferred task: {task}")
        else:
            task = "No task inferred from directory name"
            print(task)
    else:
        # If task provided via option, use it directly
        print(f"Task provided via --task option: {task}")

if __name__ == "__main__":
    main()