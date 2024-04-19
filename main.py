from pypresence import Presence
import time

# Initialize Discord RPC client with your application's client ID
client_id = '1230681469706571856'
RPC = Presence(client_id)
RPC.connect()

# Update Rich Presence with details of the program you're developing
def update_presence(program_name):
    RPC.update(
        details="Developing",
        state=f"Working on {program_name}",
        large_image="default",  # You can set custom images for your application in the Discord Developer Portal (idk the url but look it up)
        large_text="Program Development",
        start=int(time.time())
    )

# Main function to update the presence periodically
def main():
    program_name = "Your Program Name"
    update_presence(program_name)
    while True:
        time.sleep(15)  # Update presence every 15 seconds (Discord has rate limits i think?)
        update_presence(program_name)

if __name__ == "__main__":
    main()
