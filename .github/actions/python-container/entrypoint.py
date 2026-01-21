#!/usr/bin/env python3
import os, datetime as dt


# GitHub injects INPUT_NAME based on the input name
name = os.getenv("INPUT_NAME", "World")

time = dt.datetime.now(dt.timezone.utc).strftime("%H:%M:%S")
greeting = f"Hello, {name}! Time is {time} UTC."
print(greeting)

# We can use workflow commands from: https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/workflow-commands-for-github-actions
print(f"::notice file=entrypoint.py,line=13::{greeting}")

# Expose an output for downstream steps/jobs
with open(os.environ["GITHUB_OUTPUT"], "a") as fh:
    fh.write(f"time={time}\n")