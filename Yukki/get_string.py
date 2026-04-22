from pyrogram import Client

api_id = int(input("API_ID: "))
api_hash = input("API_HASH: ")

with Client("session", api_id, api_hash) as app:
    print(app.export_session_string())