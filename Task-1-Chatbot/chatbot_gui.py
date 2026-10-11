
import tkinter as tk
from tkinter import scrolledtext


def get_response(user_input):
    message = user_input.lower().strip()

    if message in ["hi", "hello", "hey"]:
        return "Hello! How can I help you?"

    elif "your name" in message:
        return "I am an AI chatbot."

    elif "how are you" in message:
        return "I am doing well! Thank you."

    elif "bye" in message:
        return "Goodbye! Have a nice day!"

    else:
        return "Sorry, I didn't understand that."


def send_message(event=None):
    message = entry.get().strip()

    if not message:
        return

    chat_area.config(state="normal")
    chat_area.insert(tk.END, "You: " + message + "\n")

    response = get_response(message)
    chat_area.insert(tk.END, "Bot: " + response + "\n\n")
    chat_area.config(state="disabled")
    chat_area.see(tk.END)

    entry.delete(0, tk.END)

    if message.lower().strip() == "bye":
        send_button.config(state="disabled")
        entry.config(state="disabled")


root = tk.Tk()
root.title("AI Chatbot")
root.geometry("500x550")
root.configure(bg="#eaf2f8")

title = tk.Label(
    root,
    text="AI Chatbot",
    font=("Arial", 20, "bold"),
    bg="#eaf2f8",
    fg="#154360"
)
title.pack(pady=12)

chat_area = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    font=("Arial", 12),
    width=50,
    height=20,
    state="disabled"
)
chat_area.pack(padx=15, pady=10, fill="both", expand=True)

bottom_frame = tk.Frame(root, bg="#eaf2f8")
bottom_frame.pack(fill="x", padx=15, pady=15)

entry = tk.Entry(bottom_frame, font=("Arial", 12))
entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
entry.bind("<Return>", send_message)

send_button = tk.Button(
    bottom_frame,
    text="Send",
    font=("Arial", 11, "bold"),
    bg="#2874a6",
    fg="white",
    command=send_message
)
send_button.pack(side="right")

chat_area.config(state="normal")
chat_area.insert(
    tk.END,
    "Bot: Hello! Welcome to the AI Chatbot.\n"
    "Bot: Type 'bye' to exit.\n\n"
)
chat_area.config(state="disabled")

entry.focus()
root.mainloop()
