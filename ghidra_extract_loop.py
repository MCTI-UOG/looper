import os
import subprocess

# Path to your Ghidra installation
ghidra_path = "C:\\path\\to\\ghidra_10.1.5_PUBLIC"  # Update with your Ghidra path
ghidra_headless_path = os.path.join(ghidra_path, "support", "analyzeHeadless.bat")

# Project directory (where Ghidra stores project data) - can be temporary
project_dir = "C:\\path\\to\\temp_project"

# Directory containing the malware samples
malware_folder = "C:\\path\\to\\malware_samples"

# Directory to save the extracted .opcode files
output_folder = "C:\\path\\to\\output_folder"

# Path to the Ghidra extraction script in the Scripts directory
script_name = "ExtractOpCodes.py"  # Name of the script saved in Ghidra’s Scripts directory

# Ensure output directory exists
os.makedirs(output_folder, exist_ok=True)

# Loop through each file in the malware folder
for filename in os.listdir(malware_folder):
    if filename.endswith(".exe") or filename.endswith(".bin"):  # Update with relevant file extensions
        file_path = os.path.join(malware_folder, filename)
        # Define the output file name based on the malware file
        output_file = os.path.join(output_folder, filename + ".opcode")
        
        # Command to run Ghidra headlessly with the extraction script
        command = [
            ghidra_headless_path,
            project_dir,
            "TempProject",
            "-import", file_path,
            "-postScript", script_name,
            output_file  # Pass the output file to the script if it accepts an output argument
        ]
        
        print(f"Running Ghidra on {filename}...")
        # Run the command
        subprocess.run(command, check=True)
        print(f"Output saved to {output_file}")

print("All files processed.")
