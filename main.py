import menu
import database

# Initialize database
database.start_db()

# Start the menu loop
menu.handle_options()
