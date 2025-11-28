#!/bin/bash

echo "Какое название для новой функции?"
read feature_name

echo "Создаю ветку $feature_name"
git checkout -b $feature_name

echo "Ветка создана! Вы на ветке $feature_name"
git branch
