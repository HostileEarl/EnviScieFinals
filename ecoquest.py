import tkinter as tk
import random
from PIL import Image, ImageTk 

# -------------------------
#   TRASH DATA
# -------------------------
trash_items = [
    # Recyclable
    ("Paper", "Recyclable"),
    ("Plastic Bottle", "Recyclable"),
    ("Cardboard", "Recyclable"),
    ("Tin Can", "Recyclable"),
    ("Glass Bottle", "Recyclable"),
    ("Newspaper", "Recyclable"),
    ("Plastic Container", "Recyclable"),
    ("Aluminum Foil", "Recyclable"),
    ("Plastic Bag", "Recyclable"),
    ("Used Paper Carton", "Recyclable"),
    ("Magazines", "Recyclable"),
    ("Soda Can", "Recyclable"),
    ("Water Bottle Cap", "Recyclable"),
    ("Plastic Wrapper", "Recyclable"),
    ("Metal Lid", "Recyclable"),
    ("Carton Box", "Recyclable"),

    # Biodegradable
    ("Banana Peel", "Biodegradable"),
    ("Apple Core", "Biodegradable"),
    ("Leftover Food", "Biodegradable"),
    ("Vegetable Scraps", "Biodegradable"),
    ("Leaves", "Biodegradable"),
    ("Eggshells", "Biodegradable"),
    ("Rice", "Biodegradable"),
    ("Fruit Peels", "Biodegradable"),
    ("Coffee Grounds", "Biodegradable"),
    ("Tea Leaves", "Biodegradable"),
    ("Bread Crumbs", "Biodegradable"),
    ("Corn Cob", "Biodegradable"),
    ("Coconut Shell", "Biodegradable"),
    ("Plant Trimmings", "Biodegradable"),
    ("Used Tea Bag", "Biodegradable"),
    ("Fish Bones", "Biodegradable"),

    # Residual
    ("Broken Glass", "Residual"),
    ("Ceramics", "Residual"),
    ("Used Tissue", "Residual"),
    ("Diapers", "Residual"),
    ("Cigarette Butts", "Residual"),
    ("Styrofoam", "Residual"),
    ("Plastic Straw", "Residual"),
    ("Plastic Spoon/Fork", "Residual"),
    ("Hair", "Residual"),
    ("Rubber Band", "Residual"),
    ("Sanitary Napkin", "Residual"),
    ("Pet Waste", "Residual"),
    ("Used Mask", "Residual"),
    ("Chip Bag", "Residual"),
    ("Candy Wrapper", "Residual"),
    ("Foil Candy Wrapper", "Residual")
]


unused_items = trash_items.copy()
score = 0
hearts = 3
current_item = None


# -------------------------
#   GAME FUNCTIONS
# -------------------------
def choose_item():
    """Choose a random item without repeating."""
    global current_item, unused_items

    if not unused_items:  # If list is empty
        trash_label.config(text="No more items! Restart game.")
        return

    current_item = random.choice(unused_items)
    unused_items.remove(current_item)

    trash_label.config(text=f"Trash Item: {current_item[0]}")


def update_hearts():
    """Update heart display."""
    hearts_label.config(text="❤ " * hearts)


def check_answer(category):
    """Check if player chose correct bin."""
    global score, hearts

    if current_item is None:
        return

    if category == current_item[1]:
        score += 1
        score_label.config(text=f"Score: {score}")
        choose_item()
    else:
        hearts -= 1
        update_hearts()

        if hearts <= 0:
            hearts_label.config(text="💔 Game Over!")
            trash_label.config(text="You ran out of hearts!")
            disable_buttons()

    
def disable_buttons():
    recyclable_btn.config(state="disabled")
    bio_btn.config(state="disabled")
    residual_btn.config(state="disabled")


def enable_buttons():
    recyclable_btn.config(state="normal")
    bio_btn.config(state="normal")
    residual_btn.config(state="normal")


def restart_game():
    """Reset everything."""
    global score, hearts, unused_items

    score = 0
    hearts = 3
    unused_items = trash_items.copy()

    score_label.config(text="Score: 0")
    update_hearts()

    enable_buttons()
    choose_item()


# -------------------------
#   GUI SETUP
# -------------------------
root = tk.Tk()
root.title("Eco-Quest: Trash Sorter")
root.state("zoomed")  # Fullscreen-like on Windows

# Make window scalable
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

main_frame = tk.Frame(root, bg="#e8f5e9")
main_frame.grid(row=0, column=0, sticky="nsew")

# Load background image
original_bg = Image.open("background.jpg")  # Replace with your image path

# Function to resize background dynamically
def resize_bg(event):
    global bg_image_tk
    new_width = event.width
    new_height = event.height
    resized = original_bg.resize((new_width, new_height))
    bg_image_tk = ImageTk.PhotoImage(resized)
    bg_label.config(image=bg_image_tk)

# Create label for background
bg_image_tk = ImageTk.PhotoImage(original_bg)
bg_label = tk.Label(main_frame, image=bg_image_tk)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Bind resize event
main_frame.bind("<Configure>", resize_bg)

# Responsive layout structure
for i in range(6):
    main_frame.rowconfigure(i, weight=1)
for i in range(3):
    main_frame.columnconfigure(i, weight=1)

title_label = tk.Label(main_frame, text="♻ ECO-QUEST: TRASH SORTER ♻",
                       font=("Helvetica", 30, "bold"), bg="#e8f5e9")
title_label.grid(row=0, column=0, columnspan=3)

trash_label = tk.Label(main_frame, text="Trash Item:",
                       font=("Helvetica", 22), bg="#e8f5e9")
trash_label.grid(row=1, column=0, columnspan=3)

score_label = tk.Label(main_frame, text="Score: 0",
                       font=("Helvetica", 20), bg="#e8f5e9")
score_label.grid(row=2, column=0, columnspan=3)

hearts_label = tk.Label(main_frame, text="❤ ❤ ❤",
                        font=("Helvetica", 28), bg="#e8f5e9")
hearts_label.grid(row=3, column=0, columnspan=3)

# CATEGORY BUTTONS
recyclable_btn = tk.Button(main_frame, text="Recyclable", font=("Helvetica", 16),
                           width=20, height=2,
                           command=lambda: check_answer("Recyclable"))
bio_btn = tk.Button(main_frame, text="Biodegradable", font=("Helvetica", 16),
                    width=20, height=2,
                    command=lambda: check_answer("Biodegradable"))
residual_btn = tk.Button(main_frame, text="Residual", font=("Helvetica", 16),
                         width=20, height=2,
                         command=lambda: check_answer("Residual"))

recyclable_btn.grid(row=4, column=0, padx=20)
bio_btn.grid(row=4, column=1, padx=20)
residual_btn.grid(row=4, column=2, padx=20)

# RESTART BUTTON
restart_btn = tk.Button(main_frame, text="Restart Game",
                        width=15, height=1, font=("Helvetica", 14),
                        command=restart_game)
restart_btn.grid(row=5, column=1, pady=20)

# Start the game
restart_game()

root.mainloop()
