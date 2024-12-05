# ANSI escape codes format: \033[<code>m
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
RESET = "\033[0m"  # ใช้คืนค่ากลับเป็นปกติ

text = f"{GREEN}This is red text{RESET}"
print(text)
