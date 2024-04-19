# simple-discord-rpc

# Set Up a Discord Application:

    Go to the Discord Developer Portal (https://discord.com/developers/applications) and create a new application.
    Note down the "Client ID" of your application, as you'll need it when running the program.

# Install Discord RPC Library:
``
    You'll need a library that allows your program to communicate with Discord's RPC API. You can install it via pip:
```
    pip install pypresence
```
# Write Your Program:

    Import the pypresence module.
    Initialize the RPC client with your Discord application's client ID.
    Update the Rich Presence with details of the program you're developing, such as the program's name, status, and any additional details you want to display.
    Periodically update the Rich Presence as needed.
