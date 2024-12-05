import tkinter as tk
from tkinter import messagebox

# ฟังก์ชันแปลง RGB เป็น Hexadecimal
def rgb_to_hex(rgb):
    return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"

# ฟังก์ชันเพื่อแสดงสีที่เลือก
def update_display_color(event=None):
    try:
        # รับค่าจากช่องกรอกข้อมูล RGB ของสีแรก
        r1 = int(entry_r1.get())
        g1 = int(entry_g1.get())
        b1 = int(entry_b1.get())
        
        # รับค่าจากช่องกรอกข้อมูล RGB ของสีที่สอง
        r2 = int(entry_r2.get())
        g2 = int(entry_g2.get())
        b2 = int(entry_b2.get())
        
        # ตรวจสอบว่าเป็นค่าที่ถูกต้องในช่วง 0-255
        if 0 <= r1 <= 255 and 0 <= g1 <= 255 and 0 <= b1 <= 255:
            color1 = (r1, g1, b1)
            color1_display.config(bg=rgb_to_hex(color1))
        else:
            color1_display.config(bg="gray")
        
        if 0 <= r2 <= 255 and 0 <= g2 <= 255 and 0 <= b2 <= 255:
            color2 = (r2, g2, b2)
            color2_display.config(bg=rgb_to_hex(color2))
        else:
            color2_display.config(bg="gray")
        
    except ValueError:
        # หากค่าไม่สามารถแปลงเป็นตัวเลขได้ ให้แสดงสีเทา
        color1_display.config(bg="gray")
        color2_display.config(bg="gray")

# ฟังก์ชันสำหรับผสมสี
def mix_colors(color1, color2):
    mixed_red = (color1[0] + color2[0]) // 2
    mixed_green = (color1[1] + color2[1]) // 2
    mixed_blue = (color1[2] + color2[2]) // 2
    return (mixed_red, mixed_green, mixed_blue)

# ฟังก์ชันเพื่อแสดงสีที่ผสม
def show_mixed_color():
    color1 = get_color_input(entry_r1, entry_g1, entry_b1)
    color2 = get_color_input(entry_r2, entry_g2, entry_b2)
    
    if color1 and color2:
        mixed_color = mix_colors(color1, color2)
        # แปลง RGB เป็น Hexadecimal และแสดงสีที่ผสม
        hex_color = rgb_to_hex(mixed_color)
        
        # แสดงสีที่ผสม
        mixed_color_display.config(bg=hex_color)
        result_label.config(text=f"Mixed Color: {mixed_color}")

# ฟังก์ชันให้ผู้ใช้ป้อนค่า RGB
def get_color_input(entry_r, entry_g, entry_b):
    try:
        r = int(entry_r.get())
        g = int(entry_g.get())
        b = int(entry_b.get())
        
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return (r, g, b)
        else:
            messagebox.showerror("Invalid Input", "Please enter values between 0 and 255.")
            return None
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid integer values.")
        return None

# สร้างหน้าต่าง GUI
root = tk.Tk()
root.title("Color Mixer")

# ตั้งขนาดหน้าต่าง
root.geometry("400x500")

# สร้างส่วนป้อนค่าของสี
frame1 = tk.LabelFrame(root, text="First Color (RGB)", padx=10, pady=10)
frame1.pack(padx=10, pady=10, fill="both", expand=True)

entry_r1 = tk.Entry(frame1, width=5)
entry_g1 = tk.Entry(frame1, width=5)
entry_b1 = tk.Entry(frame1, width=5)

entry_r1.grid(row=0, column=0, padx=5, pady=5)
entry_g1.grid(row=0, column=1, padx=5, pady=5)
entry_b1.grid(row=0, column=2, padx=5, pady=5)

frame2 = tk.LabelFrame(root, text="Second Color (RGB)", padx=10, pady=10)
frame2.pack(padx=10, pady=10, fill="both", expand=True)

entry_r2 = tk.Entry(frame2, width=5)
entry_g2 = tk.Entry(frame2, width=5)
entry_b2 = tk.Entry(frame2, width=5)

entry_r2.grid(row=0, column=0, padx=5, pady=5)
entry_g2.grid(row=0, column=1, padx=5, pady=5)
entry_b2.grid(row=0, column=2, padx=5, pady=5)

# ใช้ bind เพื่อตรวจจับการพิมพ์
entry_r1.bind("<KeyRelease>", update_display_color)
entry_g1.bind("<KeyRelease>", update_display_color)
entry_b1.bind("<KeyRelease>", update_display_color)

entry_r2.bind("<KeyRelease>", update_display_color)
entry_g2.bind("<KeyRelease>", update_display_color)
entry_b2.bind("<KeyRelease>", update_display_color)

# ปุ่มเพื่อแสดงสีที่ผสม
mix_button = tk.Button(root, text="Mix Colors", command=show_mixed_color)
mix_button.pack(pady=20)

# แสดงสีที่ผู้ใช้เลือก
color1_display = tk.Label(root, text="First Color", width=20, height=2)
color1_display.pack(pady=5)

color2_display = tk.Label(root, text="Second Color", width=20, height=2)
color2_display.pack(pady=5)

# แสดงสีที่ผสม
mixed_color_display = tk.Label(root, text="Mixed Color", width=20, height=2)
mixed_color_display.pack(pady=10)

# แสดงผลลัพธ์ที่ผสมแล้ว
result_label = tk.Label(root, text="Mixed Color: ")
result_label.pack(pady=5)

# เริ่มต้นการทำงานของโปรแกรม
root.mainloop()
