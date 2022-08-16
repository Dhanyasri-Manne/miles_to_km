from tkinter import *
def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result_label.config(text=f"{km}")

window =Tk()
window.title("Miles to Kilometer converter")
window.config(padx=25,pady=25)

miles_input = Entry(width=8)
miles_input.grid(column=1,row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2,row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0,row=1)

km_result_label =Label(text="0")
km_result_label.grid(column=1,row=1)

cal_button = Button(text="calculate",command=miles_to_km)
cal_button.grid(column=1,row=2)



window.mainloop()