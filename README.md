# DylanBennett-MS
Dylan Bennett's Microservice

Tips Publisher Service - The Tips Publisher service is a ZeroMQ driven feature of Dylan's Video Game library. Tips will allow a user to request a number of tips on how to easier use the library service. Some tips may also give suggestions on the types of video games to play.

Requirements
Python 3.x
pyzmq library for ZeroMQ
To install the required dependencies, you can run:

    bash pip install pyzmq

Example code- The array is trimmed for brevity:

    import zmq
    import random

    game_tips = [
    "You can always go back to your full list of games by clicking on the Home Button!",
    ]

    def start_publisher():
        context = zmq.Context()
        socket = context.socket(zmq.REP)

        socket.bind("tcp://*:5556")
        print("Publisher started on port 5556...")
    
        while True:
            num_tips = int(socket.recv_string())  # Receive the number of tips requested
            print(f"Received request for {num_tips} tips")

            selected_tips = random.sample(game_tips, num_tips)  # Select unique tips

            response = "\n".join(selected_tips)
            socket.send_string(response)

    if __name__ == "__main__":
        start_publisher()
        
How to Run
1. Run the Publisher Service
In your terminal, navigate to the directory where tips.py is located and run:

    bash python tips.py
   
This will start the publisher service on port 5556, and whenever it receives a request on that port with an integer parameter it will return that number of tips.

3. Request Tips with a Subscriber
A ZMQ based subscriber can send a number to the service and receive that number of tips.

Example Subscriber code:

    import zmq

    def request_tips():
        context = zmq.Context()
        socket = context.socket(zmq.REQ)  # Use REQ for request

    socket.connect("tcp://localhost:5556")
    
    while True:
        num_tips = int(input("Enter the number of tips you want (0 to exit): "))

        if num_tips == 0:
            print("Exiting the program.")
            break

        socket.send_string(str(num_tips))

        response = socket.recv_string()
        
        print("\nReceived tips:")
        print(response)

    if __name__ == "__main__":
        request_tips()


How It Works:
The subscriber asks for a certain number of tips (e.g., "How many tips do you want?").
The subscriber sends the request to the publisher via ZeroMQ.
The publisher sends back the requested number of random tips.
The subscriber receives and displays the tips.

Running the Subscriber:
To run the subscriber, execute the following:

    bash python subscriber.py
    Enter the number of tips you want: 3

Example Output:

    Received tips:
    In-person multiplayer gives you the best performance and connection stability.
    Multiplayer modes are more fun with friends; consider LAN for faster performance.
    Always check the difficulty setting before starting a new game to match your skill level.
    
Tips List
The service sends a selection of tips from the following categories:

Game Library Management:
Categorize games by genre to quickly find favorites.
Use the search function to find games faster.
Sort games by release date to see the most recent additions.
Gameplay Tips:
Use the map frequently in open-world games.
Multiplayer modes are more enjoyable with friends (consider LAN for performance).
Explore hidden areas to find easter eggs.

![image](https://github.com/user-attachments/assets/8791883a-64a8-48cd-b219-2eb9ea0a581b)

