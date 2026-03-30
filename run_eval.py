import os
import csv
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

input_file = "LLM Evaluation Workflow - Sheet1.csv"
output_file = "evaluation_output.csv"

rows_out = []

with open(input_file, "r") as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        user_input = row["INPUT"]
        
        if not user_input.strip():
            continue
        
        prompt = f"Classify the user intent in ONE short label only: {user_input}"
        
        response = model.generate_content(prompt)
        output = response.text.strip()
        
        row["OUTPUT"] = output
        
        rows_out.append(row)

with open(output_file, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(rows_out)

print("Saved to evaluation_output.csv")
