#!/bin/sh

git add .
git commit -m "TRAVIS"
git push --repo https://${GITHUB_TOKEN}@github.com/Fondamenti18/fondamenti-di-programmazione.git &> /dev/null

