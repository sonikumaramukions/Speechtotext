import tkinter as tk
import speech_recognition as sr

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = r.listen(source)
            text = r.recognize_google(audio)
            txtspeech.insert(tk.END, text + "\n")
        except sr.UnknownValueError:
            txtspeech.insert(tk.END, "Could not understand audio\n")
        except sr.RequestError as e:
            txtspeech.insert(tk.END, "Could not request results; {0}\n".format(e))

def reset_txtspeech():
    txtspeech.delete("1.0", tk.END)

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("Speech to Text")

MainFrame = tk.Frame(root, bd=20, width=300, height=300)
MainFrame.pack()

lblTitle = tk.Label(MainFrame, font=('arial', 40, 'bold'), text="Speech to Text", width=18)
lblTitle.pack()
txtspeech = tk.Text(MainFrame, font=('arial', 30, 'bold'), width=40, height=12)
txtspeech.pack()

btnConvert = tk.Button(MainFrame, font=('arial', 12, 'bold'), text="Convert to Text", width=20, height=2, command=speech_to_text)
btnConvert.pack(side=tk.LEFT, padx=2)

btnReset = tk.Button(MainFrame, font=('arial', 12, 'bold'), text="Reset", width=20, height=2, command=reset_txtspeech)
btnReset.pack(side=tk.LEFT, padx=2)

btnExit = tk.Button(MainFrame, font=('arial', 12, 'bold'), text="Exit", width=20, height=2, command=exit_app)
btnExit.pack(side=tk.LEFT, padx=2)

root.geometry("1920x1080")  # Adjust the window size to your preference
root.mainloop()
