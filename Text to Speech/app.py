import pyttsx3

def text_to_speech(file_path):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech

    # Open and read the text file
    with open(file_path, 'r') as file:
        text = file.read()

    # Use the engine to convert text to speech
    engine.say(text)

    # Wait for the speech to finish
    engine.runAndWait()

if __name__ == "__main__":
    # Specify the path to your text file
    text_file_path = "path/to/your/text_file.txt"

    # Call the function to convert text to speech
    text_to_speech(text_file_path)