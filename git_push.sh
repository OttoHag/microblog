#!/bin/bash
echo "Legger til alle endringer..."
git add .

echo "Lager commit..."
git commit -m "Automatisk commit fra bash-script"

echo "Pusher til GitHub..."
git push

echo "Ferdig!"
