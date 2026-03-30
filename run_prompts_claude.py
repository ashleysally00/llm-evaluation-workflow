import os
import csv
import anthropic
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

input_file = "prompt_set.csv"
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
            response = client.messages.create(
                model="claude-haiku-4-5-20251001",  # Fastest/cheapest model
                max_tokens=1024,
                messages=[{"role": "user", "content": user_input}]
            )
            output = response.content[0].text.strip()
        except Exception as e:
            print(f"Error: {e}")
            break

        row["OUTPUT"] = output
        rows_out.append(row)
        print(f"Processed: {user_input[:50]}...")

with open(output_file, "w", newline="") as f:
    fieldnames = reader.fieldnames
    if "OUTPUT" not in fieldnames:
        fieldnames = fieldnames + ["OUTPUT"]

    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows_out)

print("Saved to", output_file)
