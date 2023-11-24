import socket
import threading
import tkinter as tk


class Chat:
    def __init__(self,host,port):
        self.create_gui()
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host,port))
        threading_wait_msg = threading.Thread(target=self.waiting_messages)
        threading_wait_msg.start()

        self.scale_factor_x = 1.0
        self.scale_factor_y = 1.0

    def waiting_messages(self):
        while True:
            message = self.client.recv(1024).decode()
            self.chat_area.config(state=tk.NORMAL)
            self.chat_area.insert(tk.END, message + '\n')
            self.chat_area.config(state=tk.DISABLED)


    def create_gui(self):
        self.app = tk.Tk()
        self.app.title = 'Chat'
        self.app.minsize(500,450)
        self.app.maxsize(680,630)
        frame = tk.Frame(self.app)
        frame.pack(padx=10,pady=10, fill=tk.BOTH, expand=True)
        self.chat_area = tk.Text(frame,height=20,width=50,state=tk.DISABLED)
        self.chat_area.pack(padx=10,pady=10,fill=tk.BOTH,expand=True)

        self.chat_name = tk.Entry(frame,width=40)
        self.chat_name.pack(padx=10,pady=10,fill=tk.BOTH, expand=True)
        
        self.chat_mesage = tk.Entry(frame,width=40)
        self.chat_mesage.pack(padx=10,pady=10,fill=tk.BOTH, expand=True)

        self.chat_btn = tk.Button(frame,text='Send message', font=("Helvetica", 14),command=self.send_message)
        self.chat_btn.pack(padx=10,pady=10)

        frame.columnconfigure(0,weight=1)
        frame.rowconfigure(0,weight=1)

    def send_message(self):
        message_for_send = self.chat_mesage.get()
        name_for_send = self.chat_name.get()
        if message_for_send:
            send = f"name: {name_for_send}\nmessage: {message_for_send}\n\n"
            self.client.send(send.encode())  
            self.chat_mesage.delete(0,tk.END)

    def start(self):
        self.app.mainloop()

if __name__ == '__main__':
    chat = Chat('localhost',12345)
    chat.start()