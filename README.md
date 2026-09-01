---
title: "Obligatory 1 - MILENAGE"
author:
    - "Syver Borge Saksvik"
date: "2026-09-01"
---

# MILENAGE

## How to run 
I have structured my project a bit different than what you might be used to. 
I use UV as my package mangaer.
To make sure that my projects run correctly please use the following commands 

```bash
uv sync
uv run python -m src.milenage.main
```

## Development 
I started the development process with implementing all the helper functions that you had given us. 
I made sure to implement unit tests to make sure that the behavior i wanted was as expected.
Insted of using all the documentation to implement the f functions i used the TS35.206 just to se what input variables each function needed. Just by following the picture of each functions that you gave us in the powerpoint I was able to construct the f functions. 
At the end I implemented the main file where i take inn the datasets and construtcs a dict i use to run the functions. 

I am not big into commenting my code, because it creats a lot of clutter. My goal is to create a easy to read code. 

I put all the constant values in the file [constants.py](src/milenage/constants.py).
And in the folder /.github/workflows i have a .yml file that I used to run my code in github using Github Actions so that i could take of some load of my computer.

## Testing
I used pytest library to run my unit test if you want to verify that you can run it by using this command
```bash
uv run pytest
```
This might take a while to build. 

## Use of AI
I used AI to check some fault messages and helping me set up some frameworks like pytest.
I am used to Java and Kotlin with their testframeworks at my work. Also it help me to show me how it works. It also fixed some things after i tried to implement them whitout sucess. Alot of it whas help with importing some my own functions
