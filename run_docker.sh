#!/bin/bash

# Print CAT-SOOP Docker logo
echo "
\
/    /\__/\\
\__=(  o_O )=
(__________)
 |_ |_ |_ |_

  CAT-SOOP Docker Edition
"

# Function to display usage
show_usage() {
    echo "Usage: $0 [command]"
    echo "Commands:"
    echo "  up      - Start CAT-SOOP (default)"
    echo "  down    - Stop CAT-SOOP"
    echo "  build   - Rebuild the container"
    echo "  logs    - View logs"
    echo "  help    - Show this help message"
}

# Default command is 'up'
COMMAND=${1:-up}

case $COMMAND in
    "up")
        echo "Starting CAT-SOOP..."
        docker-compose -f catsoop/scripts/docker/docker-compose.yml up
        ;;
    "down")
        echo "Stopping CAT-SOOP..."
        docker-compose -f catsoop/scripts/docker/docker-compose.yml down
        ;;
    "build")
        echo "Rebuilding CAT-SOOP..."
        docker-compose -f catsoop/scripts/docker/docker-compose.yml up --build
        ;;
    "logs")
        echo "Showing CAT-SOOP logs..."
        docker-compose -f catsoop/scripts/docker/docker-compose.yml logs -f
        ;;
    "help"|"-h"|"--help")
        show_usage
        ;;
    *)
        echo "Unknown command: $COMMAND"
        show_usage
        exit 1
        ;;
esac 