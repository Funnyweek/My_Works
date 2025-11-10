#!/bin/bash

echo "Деплой приложения..."
git add .
git commit -m "готово к деплою"
git push origin master
echo "Деплой завершён!"
