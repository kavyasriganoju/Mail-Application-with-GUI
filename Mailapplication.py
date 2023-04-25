import tkinter as tk
import smtplib

def send_email():
    try:
        # Set up email server and login credentials
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email.get(), password.get())
        
        # Create message and send email
        message = f'Subject: {subject.get()}\n\n{body.get("1.0", "end")}'
        server.sendmail(sender_email.get(), recipient_email.get(), message)
        server.quit()
        
        # Clear form and show success message
        subject.delete(0, "end")
        body.delete("1.0", "end")
        status_label.config(text="Email sent successfully!", fg="green")
    except:
        # Show error message if email sending fails
        status_label.config(text="Email sending failed. Check login credentials and try again.", fg="red")

# Create main window and form
window = tk.Tk()
window.title("Mail Application")

sender_label = tk.Label(window, text="Sender Email")
sender_label.pack()
sender_email = tk.Entry(window)
sender_email.pack()

password_label = tk.Label(window, text="Password")
password_label.pack()
password = tk.Entry(window, show="*")
password.pack()

recipient_label = tk.Label(window, text="Recipient Email")
recipient_label.pack()
recipient_email = tk.Entry(window)
recipient_email.pack()

subject_label = tk.Label(window, text="Subject")
subject_label.pack()
subject = tk.Entry(window)
subject.pack()

body_label = tk.Label(window, text="Body")
body_label.pack()
body = tk.Text(window, height=10)
body.pack()

send_button = tk.Button(window, text="Send Email", command=send_email)
send_button.pack()

status_label = tk.Label(window, text="")
status_label.pack()

# Start the main event loop
window.mainloop()
