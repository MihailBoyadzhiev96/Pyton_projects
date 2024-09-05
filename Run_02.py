import subprocess
import time

# List of paths to your scripts
scripts = [
    "C:\\Users\\QA\\PycharmProjects\\AutomationTests\\Settings\\01_Video_resolution.py",
    "C:\\Users\\QA\\PycharmProjects\\AutomationTests\\Settings\\02_Video_Night-Sensitivity.py",
    # Additional script paths can be added here as needed
]

def run_script(script_path):
    try:
        # Run the script using subprocess and wait for it to finish
        result = subprocess.run(["python", script_path], capture_output=True, text=True)
        print(f"Script {script_path} finished with return code {result.returncode}")
        print(f"Output:\n{result.stdout}")
        print(f"Errors:\n{result.stderr}")

    except Exception as e:
        print(f"An error occurred while running {script_path}: {e}")

def run_all_scripts(scripts):
    for script in scripts:
        if script:  # Check if the script path is not empty
            print(f"Running script: {script}")
            run_script(script)
            print(f"Finished running script: {script}\n")
        else:
            print("Empty script path encountered. Skipping.")

if __name__ == "__main__":
    run_all_scripts(scripts)
