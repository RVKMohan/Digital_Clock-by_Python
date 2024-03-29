# creating tkinter window
window=Tk()

# This function is used to display the correct time on the label 
def update_clock():
    hours = time.strftime("%I")
    minutes = time.strftime("%M")
    seconds = time.strftime("%S")
    AM_PM = time.strftime("%p")
    Exact_time = hours + ":" +minutes +":"+seconds+" "+AM_PM   
    Digital_Clock.config(text=Exact_time)
    # This function will update time for every 1 sec
    Digital_Clock.after(1000,update_clock)
Digital_Clock = Label(window,text="00:00:00",font="Roman 100 bold")
Digital_Clock.pack()

update_clock()

# This function is to give title to window
window.title('Digital Clock')
window.mainloop()
