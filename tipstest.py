import zmq

def request_tips():
    # Set up the ZeroMQ context and request socket
    context = zmq.Context()
    socket = context.socket(zmq.REQ)  # Use REQ for request
    
    # connect on 5556
    socket.connect("tcp://localhost:5556")
    
    while True:
        # Prompt the user for the number of tips they want
        num_tips = int(input("Enter the number of tips you want (0 to exit): "))
        
        # Exit the loop if the user inputs 0
        if num_tips == 0:
            print("Exiting the program.")
            break
        
        # Send the number of tips the user wants
        socket.send_string(str(num_tips))
        
        # Receive the response (tips)
        response = socket.recv_string()
        
        print("\nReceived tips:")
        print(response)

if __name__ == "__main__":
    request_tips()
