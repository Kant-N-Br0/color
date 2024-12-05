import tkinter as tk
from tkinter import messagebox

# ฟังก์ชันสำหรับผสมสี
def mix_colors(color1, color2):
    mixed_red = (color1[0] + color2[0]) // 2
    mixed_green = (color1[1] + color2[1]) // 2
    mixed_blue = (color1[2] + color2[2]) // 2
    return (mixed_red, mixed_green, mixed_blue)

# ฟังก์ชันแปลง RGB เป็น Hexadecimal
def rgb_to_hex(rgb):
    return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"

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

# ฟังก์ชันเพื่อแสดงสีที่ผสม
def show_mixed_color():
    color1 = get_color_input(entry_r1, entry_g1, entry_b1)
    color2 = get_color_input(entry_r2, entry_g2, entry_b2)
    
    if color1 and color2:
        mixed_color = mix_colors(color1, color2)
        # แปลง RGB เป็น Hexadecimal และแสดงสีที่ผสม
        hex_color = rgb_to_hex(mixed_color)
        mixed_color_display.config(bg=hex_color)
        result_label.config(text=f"Mixed Color: {mixed_color}")

# สร้างหน้าต่าง GUI
root = tk.Tk()
root.title("Color Mixer")

# ตั้งขนาดหน้าต่าง
root.geometry("400x350")

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

# ปุ่มเพื่อแสดงสีที่ผสม
mix_button = tk.Button(root, text="Mix Colors", command=show_mixed_color)
mix_button.pack(pady=20)

# แสดงสีที่ผสม
mixed_color_display = tk.Label(root, text="Mixed Color", width=20, height=2)
mixed_color_display.pack(pady=10)

# แสดงผลลัพธ์ที่ผสมแล้ว
result_label = tk.Label(root, text="Mixed Color: ")
result_label.pack(pady=5)

# เริ่มต้นการทำงานของโปรแกรม
root.mainloop()
