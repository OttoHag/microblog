#!/bin/bash
echo "🔧 Starter installasjon av nødvendige Flask-pakker..."

source venv/bin/activate

pip install Flask
pip install Flask-SQLAlchemy
pip install Flask-Migrate
pip install python-dotenv

echo "✅ Alle pakker installert. Klar til å kjøre Flask!"

