import tkinter as tk
import smtplib

class MailApp(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Mail Application")
        self.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()

    def create_widgets(self):
        # Create labels
        tk.Label(self, text="From:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        tk.Label(self, text="To:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        tk.Label(self, text="Subject:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        tk.Label(self, text="Message:").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)

        # Create entry widgets
        self.from_entry = tk.Entry(self)
        self.from_entry.grid(row=0, column=1, padx=5, pady=5)
        self.to_entry = tk.Entry(self)
        self.to_entry.grid(row=1, column=1, padx=5, pady=5)
        self.subject_entry = tk.Entry(self)
        self.subject_entry.grid(row=2, column=1, padx=5, pady=5)
        self.message_text = tk.Text(self, height=10, width=50)
        self.message_text.grid(row=3, column=1, padx=5, pady=5)

        # Create send button
        self.send_button = tk.Button(self, text="Send", command=self.send_mail)
        self.send_button.grid(row=4, column=1, padx=5, pady=5)

    def send_mail(self):
        # Get values from entry widgets
        sender = self.from_entry.get()
        receiver = self.to_entry.get()
        subject = self.subject_entry.get()
        message = self.message_text.get("1.0", tk.END)

        # Connect to SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, 'your_password_here')

        # Compose and send email
        email = f"From: {sender}\nTo: {receiver}\nSubject: {subject}\n\n{message}"
        server.sendmail(sender, receiver, email)
        server.quit()

        # Clear entry widgets and message text
        self.from_entry.delete(0, tk.END)
        self.to_entry.delete(0, tk.END)
        self.subject_entry.delete(0, tk.END)
        self.message_text.delete("1.0", tk.END)

if __name__ == '__main__':
    root = tk.Tk()
    app = MailApp(root)
    root.mainloop()
