#!/usr/bin/env python3
import os
import sys

print("="*60)
print("🔍 DIAGNOSTIC TEST")
print("="*60)

# خواندن متغیرها
api_id = os.environ.get("API_ID", "")
api_hash = os.environ.get("API_HASH", "")
bot_token = os.environ.get("BOT_TOKEN", "")
admin_id = os.environ.get("ADMIN_ID", "")

print("\n1️⃣ Checking Environment Variables:")
print(f"   API_ID: {'✅ SET' if api_id else '❌ NOT SET'} (length: {len(api_id)})")
print(f"   API_HASH: {'✅ SET' if api_hash else '❌ NOT SET'} (length: {len(api_hash)})")
print(f"   BOT_TOKEN: {'✅ SET' if bot_token else '❌ NOT SET'} (length: {len(bot_token)})")
print(f"   ADMIN_ID: {'✅ SET' if admin_id else '❌ NOT SET'} (length: {len(admin_id)})")

# چک خالی بودن
if not api_id:
    print("\n❌ ERROR: API_ID is not set!")
    sys.exit(1)
if not api_hash:
    print("\n❌ ERROR: API_HASH is not set!")
    sys.exit(1)
if not bot_token:
    print("\n❌ ERROR: BOT_TOKEN is not set!")
    sys.exit(1)
if not admin_id:
    print("\n❌ ERROR: ADMIN_ID is not set!")
    sys.exit(1)

print("\n2️⃣ Converting API_ID to integer:")
try:
    api_id_int = int(api_id)
    print(f"   ✅ Success: {api_id_int}")
except ValueError as e:
    print(f"   ❌ Failed: {e}")
    print(f"   Value was: '{api_id}'")
    sys.exit(1)

print("\n3️⃣ Converting ADMIN_ID to integer:")
try:
    admin_id_int = int(admin_id)
    print(f"   ✅ Success: {admin_id_int}")
except ValueError as e:
    print(f"   ❌ Failed: {e}")
    print(f"   Value was: '{admin_id}'")
    sys.exit(1)

print("\n4️⃣ Importing pyrogram:")
try:
    from pyrogram import Client, filters
    print("   ✅ Import successful")
except ImportError as e:
    print(f"   ❌ Failed: {e}")
    sys.exit(1)

print("\n5️⃣ Creating Pyrogram Client:")
try:
    app = Client(
        "test_bot",
        api_id=api_id_int,
        api_hash=api_hash,
        bot_token=bot_token
    )
    print("   ✅ Client created successfully")
except Exception as e:
    print(f"   ❌ Failed: {e}")
    sys.exit(1)

print("\n6️⃣ Defining message handler:")
@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("✅ Bot is working!")

print("   ✅ Handler defined")

print("\n" + "="*60)
print("🚀 ALL TESTS PASSED! Starting bot...")
print("="*60)

try:
    print(f"👤 Admin ID: {admin_id_int}")
    app.run()
except KeyboardInterrupt:
    print("\n⛔ Stopped by user")
except Exception as e:
    print(f"\n❌ Runtime error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
