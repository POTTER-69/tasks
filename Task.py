import tkinter as tk
from gtts import gTTS
import playsound
import os
def text_to_speech():
    """When you press the green button sound will play"""
    text = entry.get()
    if text.strip():  
        try:
            tts = gTTS(text=text, lang='en')
            audio_file = "speech.mp3"
            tts.save(audio_file)
            playsound.playsound(audio_file)
            os.remove(audio_file)
        except Exception as e:
            print("Error", e)
    else:
        print("Text Empty")

def clear_text():
    """When you press black button it will delete the text"""
    entry.delete(0, tk.END)

def exit_app():
    """When you press the red button you will exit """
    root.destroy()
root = tk.Tk()
root.title("Convert text into voice")
root.geometry("400x300")  
label = tk.Label(root, text="Enter the text you want to convert", font=("Arial", 14))
label.pack(pady=20)
entry = tk.Entry(root, width=40, font=("Arial", 14))
entry.pack(pady=10)
button_frame = tk.Frame(root)
button_frame.pack(side=tk.BOTTOM, pady=30)
play_button = tk.Button(button_frame, text="Play", command=text_to_speech, bg="green", fg="white", width=10, height=2)
play_button.grid(row=0, column=0, padx=20)
exit_button = tk.Button(button_frame, text="Goodbye", command=exit_app, bg="red", fg="white", width=10, height=2)
exit_button.grid(row=0, column=1, padx=20)
set_button = tk.Button(button_frame, text="Delete", command=clear_text, bg="black", fg="white", width=10, height=2)
set_button.grid(row=0, column=2, padx=20)
root.mainloop()
