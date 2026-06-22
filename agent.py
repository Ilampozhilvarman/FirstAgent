import os
import re
import subprocess
from tools import run_research_pipeline, save_report_to_docx

os.makedirs("reports", exist_ok=True)

def main():
    while True:
        task = input("\nTask: ")
        if task.lower() == "quit":
            print("Quitting...")
            break
        
        if not task.strip():
            continue
            
        print("\n[1/4] Formulating optimized search targets...")
        print("[2/4] Gathering live web data concurrently...")
        print("[3/4] Drafting initial report & starting agentic critique loop...")
        final_report = run_research_pipeline(task)
        
        print("[4/4] Rendering polished document formatting...")
        safe_name = re.sub(r'[^a-zA-Z0-9_ ]', '', task).strip().replace(" ", "_")[:40]
        filename = f"reports/{safe_name}.docx"
        
        save_report_to_docx(task, final_report, filename)
        print(f" Success! Saved to: {filename}")
        subprocess.run(["open", filename])

if __name__ == "__main__":
    main()