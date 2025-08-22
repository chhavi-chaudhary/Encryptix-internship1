import tkinter as tk
from tkinter import scrolledtext

class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.setup_ui()
        
    def setup_ui(self):
        # Window configuration
        self.root.title("AI Chatbot")
        self.root.geometry("500x600")
        
        # Chat display area
        self.chat_area = scrolledtext.ScrolledText(
            self.root,
            wrap=tk.WORD,
            width=50,
            height=20,
            state='normal'  # Changed from disabled to allow updates
        )
        self.chat_area.pack(pady=10)
        
        # Input frame
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)
        
        # User input field
        self.entry_user_input = tk.Entry(
            input_frame,
            width=40,
            font=('Arial', 12)
        )
        self.entry_user_input.pack(side=tk.LEFT, padx=5)
        self.entry_user_input.bind("<Return>", lambda event: self.send_message())

        # Send button
        self.send_button = tk.Button(
            input_frame,
            text="Send",
            command=self.send_message,
            bg='#4CAF50',
            fg='white',
            relief=tk.RAISED
        )
        self.send_button.pack(side=tk.LEFT)

    def chatbot_response(self, user_input):
        user_input = user_input.lower()
        
        responses = {
            ('hello', 'hi', 'hey'): "Hello! How can I help you today?",
            ('how are you',): "I'm functioning well! How about you?",
            ('your name',): "I'm an AI chatbot assistant, here to help you with recommendations!",
            ('bye', 'goodbye', 'exit'): "Goodbye! Have a nice day! 😊",
            ('what can you do', 'help', 'assistance'): "I can provide recommendations on movies, books, restaurants, and more! Just ask!",
            ('recommendation', 'suggest', 'suggestion'): "I'd love to help! What are you interested in? Movies, books, or something else?",
            ('movies', 'film', 'cinema'): "Here are some great movies: The Shawshank Redemption, Inception, and The Godfather. What genre do you prefer?",
            ('books', 'book', 'reading'): "I recommend The Silent Patient, Atomic Habits, and The Midnight Library. What type of book do you like?",
            ('restaurants', 'food', 'eat'): "How about trying Italian Corner for pasta or Sushi Express for fresh sushi? What are you in the mood for?",
            ('travel', 'destination', 'vacation'): "Some amazing travel spots are Kyoto, Santorini, and Banff. Where would you like to go?",
            ('thank you', 'thanks'): "You're welcome! If you have more questions, feel free to ask!",
            ('joke', 'funny', 'make me laugh'): "Why don't scientists trust atoms? Because they make up everything! 😂",
            ('time', 'date', 'day'): "My internal clock shows: " + self.get_current_time() + ". What would you like to know?",
            ('favorite', 'best', 'top'): "I can suggest popular choices based on your interests. What are you curious about?",
            ('undefined', 'unknown', 'not clear'): "I'm still learning! Could you try asking about recommendations in specific categories?",
        }
        
        for keywords, response in responses.items():
            if any(keyword in user_input for keyword in keywords):
                return response
        
        return "I didn't understand that. Could you rephrase or ask something else?"

    def get_current_time(self):
        from datetime import datetime
        return datetime.now().strftime("%H:%M:%S")

    def send_message(self):
        user_input = self.entry_user_input.get().strip()
        
        if not user_input:
            return
            
        # Display user message
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, f"You: {user_input}\n")
        
        # Get and display bot response
        response = self.chatbot_response(user_input)
        self.chat_area.insert(tk.END, f"Bot: {response}\n")
        
        # Clear input and auto-scroll
        self.entry_user_input.delete(0, tk.END)
        self.chat_area.see(tk.END)
        self.chat_area.config(state='disabled')
        
        # Exit if goodbye
        if any(word in user_input.lower() for word in ['bye', 'goodbye', 'exit']):
            self.root.after(1500, self.root.destroy)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotApp(root)
    root.mainloop()
