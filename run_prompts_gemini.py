import os
import csv
import time
from dotenv import load_dotenv
from google import genai  # Updated SDK

# Load environment variables, including your GEMINI_API_KEY
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

input_file = "LLM Evaluation Workflow - Sheet1.csv"
output_file = "evaluation_output.csv"

rows_out = []

MAX_ROWS = 5  # Limit rows to avoid hitting free API limits

with open(input_file, "r") as f:
    reader = csv.DictReader(f)
    
    # for row in reader:  # Original: reads entire sheet
    for row in list(reader)[:MAX_ROWS]:
        user_input = row["INPUT"]
        
        if not user_input.strip():
            continue
        
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=user_input
            )
            output = response.text.strip()
        except Exception as e:
            if "429" in str(e) or "ResourceExhausted" in str(e):
                print(f"Rate limit hit: {e}")
                print("Quota likely exhausted for today. Try again tomorrow.")
                break
            raise

        row["OUTPUT"] = output
        rows_out.append(row)
        
        time.sleep(2)  # Small delay between requests to avoid per-minute limits

with open(output_file, "w", newline="") as f:
    fieldnames = reader.fieldnames
    if "OUTPUT" not in fieldnames:
        fieldnames = fieldnames + ["OUTPUT"]

    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows_out)

print("Saved to", output_file)
