from pyrogram import Client, filters 
import helpers 
import os

# Retrieve credentials from environment variables
api_id = os.environ['API_ID']
api_hash = os.environ['API_HASH']
# Note: You'll need a Telegram session name for Pyrogram
session_name = "my_zip_bot"  # Customize this

app = Client( 
    session_name,
    api_id=api_id,
    api_hash=api_hash
)

@app.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply_text("I'm a zipper bot! Send me files, and I'll zip them for you. Use /zip to get started.")

@app.on_message(filters.document) # Adapt filter for file types if needed
async def zip_handler(client, message):
    user_files = await helpers.get_files_from_user(client, message) 

    if len(user_files) > 10:
        zip_filename = helpers.create_zip(user_files)
        await helpers.upload_to_cloud(client, zip_filename)  
        os.remove(zip_filename) 
    else:
        # Create zip directly and send ... (your logic here) 

app.run()
