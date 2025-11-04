"""
Tkinter GUI Typing Speed Detector
Author: Hemant Vijay
Last Updated: 4-Nov-2025
Course: 100 Days of Code by Angela Yu
Course URL: https://www.udemy.com/course/100-days-of-code/learn/practice/1251140#overview

Description:
This desktop application tests your typing speed by measuring how many words you can
type correctly within a given time period. The application displays a sample text that
the user needs to type, and calculates the typing speed in words per minute (WPM) and
accuracy percentage.

The application uses Tkinter, which is Python's standard GUI library that comes built-in
with Python, making it perfect for creating desktop applications on Windows 11.
"""

# Import the tkinter library for creating the graphical user interface
import tkinter as tk
from tkinter import messagebox
# Import time module to track how long the user takes to type
import time
# Import random module to select random text samples for typing tests
import random

# Define the main application class that inherits from tk.Tk
# This class represents the entire typing speed detector application
class TypingSpeedDetector(tk.Tk):
    """
    Main application class for the Typing Speed Detector.
    This class creates the window, manages the user interface, and handles all
    the logic for testing typing speed and calculating results.
    """

    def __init__(self):
        """
        Constructor method that runs when the application starts.
        This sets up the window, initializes variables, and creates all the UI elements.
        """
        # Call the parent class constructor to initialize the tkinter window
        super().__init__()

        # Set the title that appears in the window's title bar
        self.title("Typing Speed Detector")

        # Set the window size to 800 pixels wide by 600 pixels tall
        self.geometry("800x600")

        # Set the background color of the window to a light blue shade
        self.config(bg="#E8F4F8")

        # Prevent the window from being resized by the user
        self.resizable(False, False)

        # Sample texts that will be used for the typing test
        # These are various sentences of different complexity levels
        self.sample_texts = [
            "The quick brown fox jumps over the lazy dog. This sentence contains every letter of the alphabet.",
            "Python is a versatile programming language that is widely used in web development, data science, and automation.",
            "Practice makes perfect. The more you type, the faster and more accurate you will become over time.",
            "Typing speed is measured in words per minute. Professional typists can achieve speeds of over 80 WPM.",
            "Regular practice and proper finger placement on the keyboard are essential for improving typing skills."
        ]

        # Variable to store the text that the user needs to type
        self.current_text = ""

        # Variable to store the time when the user starts typing
        self.start_time = None

        # Variable to track whether the test is currently running
        self.test_in_progress = False

        # Create all the user interface elements (buttons, labels, text boxes, etc.)
        self.create_widgets()

    def create_widgets(self):
        """
        This method creates all the visual elements (widgets) of the application.
        It sets up the title, instructions, text displays, input field, and buttons.
        """

        # Create the main title label at the top of the window
        title_label = tk.Label(
            self,
            text="Typing Speed Detector",
            font=("Helvetica", 28, "bold"),
            bg="#E8F4F8",
            fg="#2C3E50"
        )
        # Place the title label with padding around it
        title_label.pack(pady=20)

        # Create a label to show instructions to the user
        instruction_label = tk.Label(
            self,
            text="Click 'Start Test' to begin. Type the text shown below as quickly and accurately as possible.",
            font=("Helvetica", 11),
            bg="#E8F4F8",
            fg="#34495E",
            wraplength=700
        )
        instruction_label.pack(pady=10)

        # Create a frame (container) to hold the sample text display
        text_frame = tk.Frame(self, bg="#FFFFFF", relief=tk.RIDGE, borderwidth=3)
        text_frame.pack(pady=15, padx=40, fill=tk.BOTH, expand=False)

        # Create a label to display the text that the user needs to type
        # This text is read-only and shown for reference
        self.sample_text_label = tk.Label(
            text_frame,
            text="Click 'Start Test' to see the text you need to type",
            font=("Courier", 12),
            bg="#FFFFFF",
            fg="#2C3E50",
            wraplength=680,
            justify=tk.LEFT,
            padx=15,
            pady=15
        )
        self.sample_text_label.pack(fill=tk.BOTH, expand=True)

        # Create a label that appears above the input box
        input_label = tk.Label(
            self,
            text="Type here:",
            font=("Helvetica", 12, "bold"),
            bg="#E8F4F8",
            fg="#2C3E50"
        )
        input_label.pack(pady=(15, 5))

        # Create a text widget where the user will type their response
        # This is a multi-line text input box
        self.input_text = tk.Text(
            self,
            height=8,
            width=80,
            font=("Courier", 11),
            wrap=tk.WORD,
            relief=tk.RIDGE,
            borderwidth=3
        )
        self.input_text.pack(pady=10, padx=40)

        # Initially disable the input box until the test starts
        self.input_text.config(state=tk.DISABLED)

        # Bind an event so that when the user starts typing, we record the start time
        # This event triggers when any key is pressed in the input box
        self.input_text.bind("<KeyPress>", self.on_first_key_press)

        # Create a frame to hold the buttons horizontally
        button_frame = tk.Frame(self, bg="#E8F4F8")
        button_frame.pack(pady=20)

        # Create the "Start Test" button
        self.start_button = tk.Button(
            button_frame,
            text="Start Test",
            font=("Helvetica", 12, "bold"),
            bg="#3498DB",
            fg="white",
            padx=20,
            pady=10,
            command=self.start_test,
            cursor="hand2"
        )
        self.start_button.grid(row=0, column=0, padx=10)

        # Create the "Submit" button (initially disabled)
        self.submit_button = tk.Button(
            button_frame,
            text="Submit",
            font=("Helvetica", 12, "bold"),
            bg="#2ECC71",
            fg="white",
            padx=20,
            pady=10,
            command=self.submit_test,
            cursor="hand2",
            state=tk.DISABLED
        )
        self.submit_button.grid(row=0, column=1, padx=10)

        # Create the "Reset" button
        self.reset_button = tk.Button(
            button_frame,
            text="Reset",
            font=("Helvetica", 12, "bold"),
            bg="#E74C3C",
            fg="white",
            padx=20,
            pady=10,
            command=self.reset_test,
            cursor="hand2"
        )
        self.reset_button.grid(row=0, column=2, padx=10)

        # Create a label to display the results after the test
        self.result_label = tk.Label(
            self,
            text="",
            font=("Helvetica", 12),
            bg="#E8F4F8",
            fg="#2C3E50"
        )
        self.result_label.pack(pady=10)

    def start_test(self):
        """
        This method is called when the user clicks the "Start Test" button.
        It prepares a new typing test by selecting random text and enabling the input box.
        """

        # Select a random text from the list of sample texts
        self.current_text = random.choice(self.sample_texts)

        # Display the selected text in the sample text label
        self.sample_text_label.config(text=self.current_text)

        # Enable the input text box so the user can start typing
        self.input_text.config(state=tk.NORMAL)

        # Clear any previous text in the input box
        self.input_text.delete("1.0", tk.END)

        # Set focus to the input box so the user can immediately start typing
        self.input_text.focus()

        # Reset the start time (will be set when user starts typing)
        self.start_time = None

        # Mark that the test is now in progress
        self.test_in_progress = True

        # Enable the submit button so the user can submit when done
        self.submit_button.config(state=tk.NORMAL)

        # Clear any previous results
        self.result_label.config(text="")

    def on_first_key_press(self, event):
        """
        This method is called when the user presses any key in the input box.
        It records the start time when the user begins typing for the first time.

        Parameters:
        event: The keyboard event that triggered this method
        """

        # Only record the start time once (when the test just started)
        if self.test_in_progress and self.start_time is None:
            # Record the current time as the start time
            self.start_time = time.time()

    def submit_test(self):
        """
        This method is called when the user clicks the "Submit" button.
        It calculates the typing speed (WPM), accuracy, and displays the results.
        """

        # Check if the test is in progress
        if not self.test_in_progress:
            return

        # Check if the user actually started typing
        if self.start_time is None:
            # Show a warning message if no typing was detected
            messagebox.showwarning("No Input", "You haven't started typing yet!")
            return

        # Record the time when the user finished (current time)
        end_time = time.time()

        # Calculate how many seconds elapsed from start to finish
        time_elapsed = end_time - self.start_time

        # Get the text that the user typed from the input box
        typed_text = self.input_text.get("1.0", tk.END).strip()

        # Check if the user typed anything
        if not typed_text:
            messagebox.showwarning("No Input", "You haven't typed anything!")
            return

        # Calculate the typing speed and accuracy
        wpm, accuracy = self.calculate_results(typed_text, time_elapsed)

        # Display the results to the user
        result_text = f"Time: {time_elapsed:.2f} seconds | Speed: {wpm:.2f} WPM | Accuracy: {accuracy:.2f}%"
        self.result_label.config(text=result_text)

        # Disable the input box and submit button after submission
        self.input_text.config(state=tk.DISABLED)
        self.submit_button.config(state=tk.DISABLED)

        # Mark the test as no longer in progress
        self.test_in_progress = False

        # Show a popup message with the results
        messagebox.showinfo(
            "Test Results",
            f"Typing Speed: {wpm:.2f} WPM\nAccuracy: {accuracy:.2f}%\nTime Taken: {time_elapsed:.2f} seconds"
        )

    def calculate_results(self, typed_text, time_elapsed):
        """
        This method calculates the words per minute (WPM) and accuracy percentage.

        Parameters:
        typed_text: The text that the user typed
        time_elapsed: The number of seconds it took to type

        Returns:
        A tuple containing (WPM, accuracy percentage)
        """

        # Split the sample text into individual words
        original_words = self.current_text.split()

        # Split the typed text into individual words
        typed_words = typed_text.split()

        # Count the total number of words the user typed
        total_typed_words = len(typed_words)

        # Calculate Words Per Minute (WPM)
        # Formula: (number of words typed / seconds elapsed) * 60
        # We multiply by 60 to convert from words per second to words per minute
        minutes_elapsed = time_elapsed / 60
        wpm = total_typed_words / minutes_elapsed if minutes_elapsed > 0 else 0

        # Calculate accuracy by comparing typed words with original words
        correct_chars = 0
        total_chars = len(self.current_text)

        # Compare each character in the typed text with the original text
        for i, char in enumerate(typed_text):
            # Check if we haven't exceeded the original text length
            if i < len(self.current_text):
                # If the character matches, increment the correct count
                if char == self.current_text[i]:
                    correct_chars += 1

        # Calculate accuracy percentage
        # Formula: (correct characters / total characters in original text) * 100
        accuracy = (correct_chars / total_chars * 100) if total_chars > 0 else 0

        # Return both WPM and accuracy as a tuple
        return wpm, accuracy

    def reset_test(self):
        """
        This method is called when the user clicks the "Reset" button.
        It clears all fields and resets the application to its initial state.
        """

        # Clear the sample text display
        self.sample_text_label.config(text="Click 'Start Test' to see the text you need to type")

        # Clear the input text box
        self.input_text.delete("1.0", tk.END)

        # Disable the input text box
        self.input_text.config(state=tk.DISABLED)

        # Clear the results display
        self.result_label.config(text="")

        # Reset the start time
        self.start_time = None

        # Mark the test as not in progress
        self.test_in_progress = False

        # Disable the submit button
        self.submit_button.config(state=tk.DISABLED)

        # Clear the current text
        self.current_text = ""


# This is the entry point of the application
# The code below only runs if this file is executed directly (not imported)
if __name__ == "__main__":
    # Create an instance of the TypingSpeedDetector application
    app = TypingSpeedDetector()

    # Start the application's main event loop
    # This keeps the window open and responsive to user interactions
    app.mainloop()
