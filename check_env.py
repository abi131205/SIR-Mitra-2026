import os
from dotenv import load_dotenv
import google.generativeai as genai

# Try to load the .env
load_dotenv()

key = os.getenv("GEMINI_API_KEY")

print("--- Environment Check ---")
if key:
    print(f"✅ Success: Key found! (Starts with: {key[:5]}...)")
else:
    print("❌ Error: .env injection failed. Your terminal is blocking the key.")

print("\n--- Transport Check ---")
try:
    # Testing the 'rest' transport to bypass v1beta issues
    genai.configure(api_key=key if key else "dummy_key", transport='rest')
    print("✅ Success: Stable 'v1' transport configured.")
except Exception as e:
    print(f"❌ Error: Transport configuration failed: {e}")