#!/bin/bash

echo "Создание нового проекта..."
read project_name

mkdir $project_name
cd $project_name

touch main.py
touch README.md
git init

echo "Проект $project_name создан!"
