#!/bin/bash
# Local development run script

set -e

echo "🚀 Starting python-probe..."

# Check if venv exists, create if not
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python -m venv venv
fi

# Activate venv
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -q -r requirements.txt

# Load environment variables if .env exists
if [ -f ".env" ]; then
    echo "⚙️  Loading environment variables from .env"
    set -a
    source .env
    set +a
fi

# Run the app
echo "✅ Starting Flask app on http://localhost:${PORT:-8080}"
python src/app.py
