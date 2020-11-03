import tkinter as tk
from playsound import playsound
import threading
import record_keeper
import time


class Pomodoro(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.show_widgets()
        self.seconds_left = 1500
        self._timer_on = False
        self.run_set = True
        self.entered_min = int(self.ent_pom.get()) * 60

    def create_widgets(self):
        self.lbl_npom = tk.Label(self, text=f"Complete: ", font=(None, 10), padx=3)
        self.lbl_category = tk.Label(self, text="Category: ", font=(None, 10), padx=3)
        self.btn_start =tk.Button(self, text="Start", relief=tk.RAISED, font=(None, 10), bg="green", command=self.start_button) 
        self.btn_stop =tk.Button(self, text="Stop", relief=tk.RAISED, font=(None, 10), bg='orange', command=self.stop_timer) 
        self.lbl_time = tk.Label(self, text=f"25:00", relief=tk.SUNKEN, font=(None, 20), padx=15)
        self.btn_pom = tk.Button(self, text="POMO", relief=tk.RAISED, font=(None, 10), command=self.pom_button)
        self.btn_short = tk.Button(self, text="Short", relief=tk.RAISED, font=(None, 10), command=self.short_button)
        self.btn_long = tk.Button(self, text="Long", relief=tk.RAISED, font=(None, 10), command=self.long_button)

        self.ent_pom = tk.Entry(self, width=10)
        self.ent_pom.insert(0, 25)
        self.ent_pom.focus_set()
        self.ent_short = tk.Entry(self, width=10)
        self.ent_short.insert(0, 5)
        self.ent_short.focus_set()
        self.ent_long = tk.Entry(self, width=10)
        self.ent_long.insert(0, 15)
        self.ent_long.focus_set()
        self.ent_category = tk.Entry(self, width=15)
        self.ent_category.insert(0, "Coding")
        self.ent_category.focus_set()
                
    def show_widgets(self):    
        self.lbl_npom.grid(row=0, column=1, pady=2)
        self.btn_start.grid(row=1, column=0)
        self.btn_stop.grid(row=1, column=2) 
        self.lbl_time.grid(row=1, column=1, pady=5)

        self.btn_pom.grid(row=2, column=0)
        self.btn_short.grid(row=2, column=1)
        self.btn_long.grid(row=2, column=2)

        self.ent_pom.grid(row=3, column=0, pady=5)
        self.ent_short.grid(row=3, column=1, pady=5)
        self.ent_long.grid(row=3, column=2, pady=5)
        
        self.lbl_category.grid(row=4, column=0, pady=2)
        self.ent_category.grid(row=4, column=1, pady=2)


    def countdown(self):
        self.lbl_time['text'] = self.convert_minutes()

        if self.seconds_left:
            self.seconds_left -= 1
            self._timer_on = self.after(1000, self.countdown)
            if self.seconds_left <= 0 and self._timer_on:
                self.thread_sn()
                if self.run_set:
                    self.thread_rec()
                    self.lbl_npom['text'] = f"Complete: {record_keeper.check_set_number(time.time())}"
                
        else:
            self._timer_on = False

    def start_button(self):
        self.stop_timer()
        self.countdown()

    def stop_timer(self):
        if self._timer_on:
            self.after_cancel(self._timer_on)
            self._timer_on = False

    def pom_button(self):
        self.seconds_left = int(self.ent_pom.get()) * 60
        self.lbl_time['text'] = self.convert_minutes()
        self.run_set = True
        self.entered_min = self.ent_pom.get()
        self.start_button()

    def short_button(self):
        self.seconds_left = int(self.ent_short.get()) * 60
        self.lbl_time['text'] = self.convert_minutes()
        self.run_set = False
        self.start_button()

    def long_button(self):
        self.seconds_left = int(self.ent_long.get()) * 60
        self.lbl_time['text'] = self.convert_minutes()
        self.run_set = False
        self.start_button()

    def convert_minutes(self):
        return f"{self.seconds_left//60:02.0f}:{self.seconds_left % 60:02}"

    def thread_sn(self):
        threadsound = threading.Thread(target=playsound("alarm.mp3"))
        threadsound.start()
        
    def thread_rec(self):
        record = threading.Thread(
            target=record_keeper.saving_result(
                time.strftime('%Y-%m-%d', time.localtime()), 
                time.strftime('%I:%M %p', time.localtime()),
                self.entered_min, self.ent_category.get())
            )
        record.start()
    

if __name__ == '__main__':
    root = tk.Tk()
    pomodoro = Pomodoro(root)
    p1 = tk.PhotoImage(file = 'icon.png')
    root.iconphoto(False, p1)
    root.title('Pomodoro')
    pomodoro.grid()
    root.mainloop()

