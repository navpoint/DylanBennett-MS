import zmq
import random

# Tips array
game_tips = [
    "You can always go back to your full list of games by clicking on the Home Button!",
    "You can sort your list of games by name, genre, or year.",
    "When adding game art to a new game, you can either browse your files for game art, or you can drag and drop art.",
    "If you don't have art for a game, don't worry! Placeholder art will be used instead.",
    "Make sure to categorize your games by genre to quickly find your favorites.",
    "Use the search function in your game library to find specific titles faster.",
    "Check game ratings and reviews to see what others think before downloading or purchasing a game.",
    "Organize your games by multiplayer options like 'Online', 'LAN', or 'In-Person' for quicker access to the type of play you want.",
    "Create a wishlist for games you're interested in to keep track of new releases and upcoming sales.",
    "Sort your game library by release date to always see the most recent games you've added.",
    "Consider using 'Collections' to group your games by similar themes, like 'RPGs', 'Action', or 'Indie'.",
    "Use tags to add more detail to your game collection, making it easier to filter by preferences like 'Hardcore', 'Strategy', or 'Co-op'.",
    "If your library allows, mark games you've completed to distinguish them from those you're still working on.",
    "Use the map frequently to avoid getting lost in large open-world games.",
    "Multiplayer modes are more fun with friends; consider LAN for faster performance.",
    "Always check the difficulty setting before starting a new game to match your skill level.",
    "Many games have hidden easter eggs; try exploring every nook and cranny.",
    "Before jumping into online modes, check the server type: public servers are often more crowded.",
    "Games like RPGs often allow you to modify difficulty mid-game, so feel free to experiment.",
    "Check game forums for community tips and tricks that can improve your gameplay.",
    "In-person multiplayer gives you the best performance and connection stability.",
    "Many online games allow custom servers, perfect for unique gaming experiences with friends."
]

def start_publisher():
    # Set up ZeroMQ context and socket
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    
    # Bind to port 5556
    socket.bind("tcp://*:5556")
    print("Publisher started on port 5556...")
    
    while True:
        # Wait for a request from a subscriber
        num_tips = int(socket.recv_string())  # Receive the number of tips requested
        print(f"Received request for {num_tips} tips")

        # Select random tips
        selected_tips = random.sample(game_tips, num_tips)  # Select unique tips
        

        # Send the selected tips back to the subscriber
        response = "\n".join(selected_tips)
        socket.send_string(response)

if __name__ == "__main__":
    start_publisher()
