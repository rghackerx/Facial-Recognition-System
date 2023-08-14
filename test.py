import tkinter as tk
import subprocess as sp
from otp import generate_otp  # Import the otp.py's generate_otp function

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Facial Recognition Database System")
    window.geometry("800x600")

    def otp_window():

        otp_label.place(x=10, y=170)
        otp_entry.place(x=90, y=170)
        otp_submit_button.place(x=100, y=210)
        result_label.place(x=10, y=240)

    def run():
        inp = e1.get()
        inp2 = e2.get()
        with open('creds.txt', 'w') as file:
            file.writelines(inp + "\n")
            file.writelines(inp2)
        otp_window()
        show_otp_input()

    def show_otp_input():
        otp = generate_otp()  # Generate OTP using the imported function
        otp_label.config(text="Enter OTP:")
        otp_entry.delete(0, tk.END)  # Clear any previous input
        # Enable the Submit OTP button
        otp_submit_button.config(state=tk.NORMAL)
        result_label.config(text="")
        generated_otp.set(otp)  # Set the generated OTP to the StringVar

    def verify_otp():
        entered_otp = otp_entry.get()
        correct_otp = generated_otp.get()
        print(correct_otp)

        if entered_otp == correct_otp:
            result_label.config(
                text="OTP verification successful.", fg="green")
        else:
            result_label.config(text="OTP verification failed.", fg="red")

    generated_otp = tk.StringVar()  # Variable to hold the generated OTP

    label = tk.Label(window, text="Enter Details")
    label.place(x=5, y=20)

    user = tk.Label(window, text="Username: ")
    user.place(x=10, y=70)
    e1 = tk.Entry(window, width=40)
    e1.place(x=90, y=70)

    passw = tk.Label(window, text="Password: ")
    passw.place(x=10, y=93)
    e2 = tk.Entry(window, show='*', width=40)
    e2.place(x=90, y=95)

    button = tk.Button(window, text="Submit", command=run)
    button.place(x=100, y=130)

    otp_label = tk.Label(window, text="Enter OTP:")
    otp_entry = tk.Entry(window)
    otp_submit_button = tk.Button(
        window, text="Submit OTP", command=verify_otp, state=tk.DISABLED)
    result_label = tk.Label(window, text="", fg="black")
    
    window.mainloop()
