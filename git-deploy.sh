#!/bin/bash
git status
git add *
echo "Your commit message:"
read commitmessage
echo "Here is your commit message: $commitmessage"
git commit -m $commitmessage
git push origin main
