# Cloud Computing Project 3

## Overview
This project consists of a python script, as well as a Dockerfile to run it. The docker image is based off the latest [Python Alpine image](https://hub.docker.com/_/python/).

## Process
The Docker container works as follows:
1. Launches shell script
2. Calls python script and redirects output to `/home/output/result.txt`
3. Displays the output file to `stdout` using `cat`
4. Waits in an infinite loop until the user interrupts with `CTRL + C`

## Building
1. From the root of the project directory, run:
```bash
docker build -t proj3 .
```

## Running
1. Run:
```bash
docker run proj3
```
Or, for detatched mode:
```bash
docker run -d proj3
```

## Stats:
Container size:

- 53MB (uncompressed)
- 19MB (compressed)