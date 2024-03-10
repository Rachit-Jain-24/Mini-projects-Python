import tkinter as tk
from PIL import ImageTk, Image

def generate_sapid():
    name = name_entry.get()
    batch = batch_entry.get()
    batch_year_jr = batch[-2:]
    sapid = hash(name)%10 
    rollno = hash(name + batch)%10

    if batch == '2022':
        sapid_label.config(text=f"Your SAPID is: 7057{batch_year_jr}000{sapid}")
        rollno_label.config(text=f"Your Roll Number is: L0{rollno}")
    elif batch == '2023':
        sapid_label.config(text=f"Your SAPID is: 7057{batch_year_jr}000{sapid}")
        rollno_label.config(text=f"Your Roll Number is: L0{rollno}")
    else:
        sapid_label.config(text="Sorry, we don't have admissions for that year.")
        rollno_label.config(text="")

window = tk.Tk()
window.title("SAPID and Roll Number Generator")

name_label = tk.Label(window, text="Enter your name:")
name_label.pack()

name_entry = tk.Entry(window)
name_entry.pack()

batch_label = tk.Label(window, text="Enter your batch year:")
batch_label.pack()

batch_entry = tk.Entry(window)
batch_entry.pack()

generate_button = tk.Button(window, text="Generate", command=generate_sapid)
generate_button.pack()

sapid_label = tk.Label(window, text="")
sapid_label.pack()

rollno_label = tk.Label(window, text="")
rollno_label.pack()

image = Image.open("C:/NMIMS B.TECH CSDS/logos/NMBACK.png")  # Replace "path_to_your_image.jpg" with the actual path to your image
image = image.resize((200, 200))  # Resize the image if needed
photo = ImageTk.PhotoImage(image)

image_label = tk.Label(window, image=photo)
image_label.pack()

window.mainloop()
