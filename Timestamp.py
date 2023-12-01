import time

def create_timestamp_file():
    # Get the current time in seconds since the epoch
    current_time_seconds = time.time()

    # Convert the time to a readable timestamp
    current_timestamp = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime(current_time_seconds))

    # Create a filename with the timestamp
    filename = f"timestamp_{current_timestamp}.txt"

    # Write the timestamp to the file
    with open(filename, 'w') as file:
        file.write(current_timestamp)

    print(f"File '{filename}' has been created with the content: {current_timestamp}")

# Call the function to create the timestamp file
create_timestamp_file()
