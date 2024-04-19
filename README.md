# Simple Discord Rich Presence Client

## Set Up the Discord back-end Application:

Go to the Discord Developer Portal (https://discord.com/developers/applications) and create a new application.
Note down the "Client ID" of your application, as you'll need it when running the program.

## Install Discord RPC Library:

You'll need to install discord-rpc to communicate with Discord's RPC API. You can install it via pip:
```
pip install pypresence
```
## Configuring the Program:

Replace `'YOUR_CLIENT_ID'` with the client ID of your Discord application obtained from the Discord Developer Portal. Also, customize the program_name variable with the name of the program you're developing.

## How the program works:

~ Import the pypresence module.
~ Initialize the RPC client with your Discord application's client ID.
~ Update the Rich Presence with details of the program you're developing, such as the program's name, status, and any additional details you want to display.
~ Periodically update the Rich Presence as needed.

This script continuously updates your Discord Rich Presence with the specified program name and status. Make sure to keep your Discord application's Rich Presence enabled in the Discord settings for it to display properly.
