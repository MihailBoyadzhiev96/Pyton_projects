import serial
import time
import os
import tkinter as tk
from tkinter import messagebox

# Define the log file directory
log_dir = r"C:\Users\QA\Desktop\Pyton_Test_logs"


# Function to get the next log filename
def get_next_log_filename(log_dir, base_filename="log", extension=".txt"):
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    i = 1
    while True:
        filename = f"{base_filename}{i}{extension}"
        full_path = os.path.join(log_dir, filename)
        if not os.path.exists(full_path):
            return full_path
        i += 1

# Function to show the success message box
def show_success_message():
    root = tk.Tk()
    root.withdraw()  # Hide the main Tkinter window
    messagebox.showinfo("TEST RESULT", "The test has completed successfully.")
    root.destroy()  # Destroy the Tkinter root window


# Function to log UART data
def log_uart_data(port, baudrate, log_dir, expected_responses):
    try:
        ser = serial.Serial(port, baudrate, timeout=2)  # Timeout set to 2 seconds
        print(f"Connected to {port} at {baudrate} baud.")

        if ser.is_open:
            print(f"Serial port {port} is open.")

            # Clear any existing data from the buffer
            ser.flushInput()

            log_file_path = get_next_log_filename(log_dir)

            with open(log_file_path, 'a') as log_file:
                print(f"Logging to file: {log_file_path}")

                while True:  # Infinite loop to restart from the first command if needed
                    for command, expected_response_list in zip(commands, expected_responses):
                        # 1-second delay before sending the next command
                        time.sleep(1)

                        # Send the command to the device
                        print(f"Sending command: {command}")
                        full_command = (command + '\r\n').encode('utf-8')
                        ser.write(full_command)
                        ser.flush()  # Ensure command is sent

                        # Wait for the expected response
                        response = ""
                        timeout = 10  # Set a timeout for waiting for the response
                        start_time = time.time()

                        while (time.time() - start_time) < timeout:
                            if ser.in_waiting > 0:
                                response += ser.read(ser.in_waiting).decode('utf-8')
                                if any(expected_response in response for expected_response in expected_response_list):
                                    print(f"One of the expected responses received. Proceeding to next command.")
                                    break
                            time.sleep(0.1)  # Short sleep to prevent busy waiting

                        # Check for the specific success response
                        if "-----Save settings to XML-----" in response:
                            print("Success condition met. Stopping script.")
                            show_success_message()
                            return  # Exit the script

                        if not any(expected_response in response for expected_response in expected_response_list):
                            print(f"None of the expected responses received or incorrect. Restarting from first command.")
                            # Log the incorrect response
                            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                            log_entry = f"{timestamp} - Command Sent: {command}\n{timestamp} - Incorrect Response: {response.strip()}\n"
                            log_file.write(log_entry)
                            log_file.flush()

                        # Log the correct response only if it is not the stopping condition
                        if "SCALES TASK RESUMED" not in response:
                            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                            log_entry = f"{timestamp} - Command Sent: {command}\n{timestamp} - Response: {response.strip()}\n"
                            log_file.write(log_entry)
                            log_file.flush()

        else:
            print(f"Failed to open serial port {port}.")

    except serial.SerialException as e:
        print(f"Serial error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()
            print("Serial port closed.")

# Main block to call the log_uart_data function
if __name__ == "__main__":
    commands = [
        't svc atn buttons ok',
        't svc atn buttons left',
        't svc atn buttons left',
        't svc atn buttons ok',
        't svc atn buttons right',
        't svc atn buttons right',
        't svc atn buttons down',
        # 't svc atn buttons ok',
        # 't svc atn buttons down',
        # 't svc atn buttons ok',
        't svc atn buttons down',
        # 't svc atn buttons ok',
        # 't svc atn buttons ok',
        't svc atn buttons down',
        # 't svc atn buttons ok',
        # 't svc atn buttons ok',
        't svc atn buttons down',
        # 't svc atn buttons ok',
        # 't svc atn buttons ok',
        't svc atn buttons down',
        # 't svc atn buttons ok',
        # 't svc atn buttons up',
        # 't svc atn buttons func1',
        't svc atn buttons down',
        't svc atn buttons ok',
        't svc atn buttons ok',
        't svc atn buttons ok',
        # 't svc atn buttons down',
        # 't svc atn buttons ok',
        # 't svc atn buttons ok',
        # 't svc atn buttons down',
        # 't svc atn buttons ok',
        # 't svc atn buttons ok',
        't svc atn buttons func1',
        't svc atn buttons func1'

    ]

    expected_responses = [
        ["RECEIVE INTERNAL MSG CAROUSEL TASK = 54", "RECEIVE INTERNAL MSG CAROUSEL TASK = 47"],
        ["RECEIVE INTERNAL MSG CAROUSEL TASK = 6"],
        ["RECEIVE INTERNAL MSG CAROUSEL TASK = 6"],
        ["RECEIVE INTERNAL SYS MENU TASK = 58", "RECEIVE INTERNAL MSG CAROUSEL TASK = 51"],
        ["RECEIVE INTERNAL SYS MENU TASK = 8"],
        ["RECEIVE INTERNAL SYS MENU TASK = 8"],
        ["RECEIVE INTERNAL SYS MENU TASK = 4"],
        # ["one = 1 two = 0"],
        # ["RECEIVE INTERNAL SYS MENU TASK = 4"],
        # ["one = 0 two = 0"],
        ["RECEIVE INTERNAL SYS MENU TASK = 4"],
        # ["one = 1 two = 0"],
        # ["one = 0 two = 0"],
        ["RECEIVE INTERNAL SYS MENU TASK = 4"],
        # ["one = 1 two = 0"],
        # ["one = 0 two = 0"],
        ["RECEIVE INTERNAL SYS MENU TASK = 4"],
        # ["one = 1 two = 0"],
        # ["one = 0 two = 0"],
        ["RECEIVE INTERNAL SYS MENU TASK = 4"],
        # ["one = 1 two = 0"],
        # ["RECEIVE INTERNAL SYS MENU TASK = 2"],
        # ["one = 0 two = 0"],
        ["RECEIVE INTERNAL SYS MENU TASK = 4"],
        ["RECEIVE INTERNAL SYS MENU TASK = 12"],
        ["RECEIVE INTERNAL SYS MENU TASK = 12"],
        ["RECEIVE INTERNAL SYS MENU TASK = 58"],
        # ["RECEIVE INTERNAL SYS MENU TASK = 4"],
        # ["RECEIVE INTERNAL SYS MENU TASK = 12"],
        # ["one = 0 two = 0"],
        # ["RECEIVE INTERNAL SYS MENU TASK = 4"],
        # ["one = 1 two = 0"],
        # ["one = 0 two = 0"],
        ["RECEIVE INTERNAL SYS MENU TASK = 13"],
        ["SCALES TASK RESUMED"]

    ]

    log_uart_data(port="COM4", baudrate=115200, log_dir=log_dir, expected_responses=expected_responses)