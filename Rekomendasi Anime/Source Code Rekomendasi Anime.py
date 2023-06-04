import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from collections import deque

class AnimeRecommendationApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Anime Recommendation")

# Dictionary of anime
anime_genres = {
    'Action': [
        {'title': 'Attack on Titan','year': 2013,'studio': 'Wit Studio','image': 'attack_on_titan.jpg', 'rating': 8.8},
        {'title': 'One Piece', 'year': 1999, 'studio': 'Toei Animation', 'image': 'one_piece.jpg', 'rating': 8.6},
        {'title': 'Demon Slayer', 'year': 2019, 'studio': 'ufotable', 'image': 'demon_slayer.jpg', 'rating': 8.5}
    ],
    'Comedy': [
        {'title': 'One Punch Man', 'year': 2015, 'studio': 'Madhouse', 'image': 'one_punch_man.jpg', 'rating': 8.5},
        {'title': 'Gintama', 'year': 2006, 'studio': 'Sunrise', 'image': 'gintama.jpg', 'rating' : 8.8},
        {'title': 'Nichijou', 'year': 2011, 'studio': 'Kyoto Animation', 'image': 'nichijou.jpg', 'rating': 8.3}
    ],
    'Drama': [
        {'title': 'Your Lie in April', 'year': 2014, 'studio': 'A-1 Pictures', 'image': 'your_lie_in_april.jpg', 'rating': 8.6},
        {'title': 'Clannad', 'year': 2007, 'studio': 'Kyoto Animation', 'image': 'clannad.jpg', 'rating': 8.0},
        {'title': 'Steins;Gate', 'year': 2011, 'studio': 'White Fox', 'image': 'steins_gate.jpg', 'rating': 9.0}
    ],
    'Fantasy': [
        {'title': 'Fullmetal Alchemist: Brotherhood', 'year': 2009, 'studio': 'Bones', 'image': 'fullmetal_alchemist.jpg', 'rating': 9.1},
        {'title': 'Naruto', 'year': 2002, 'studio': 'Studio Pierrot', 'image': 'naruto.jpg', 'rating': 8.2},
        {'title': 'Sword Art Online', 'year': 2012, 'studio': 'A-1 Pictures', 'image': 'sword_art_online.jpg', 'rating': 8.1}
    ],
    'Romance': [
        {'title': 'Your Name', 'year': 2016, 'studio': 'CoMix Wave Films', 'image': 'your_name.jpg', 'rating': 8.8},
        {'title': 'A Silent Voice', 'year': 2016, 'studio': 'Kyoto Animation', 'image': 'a_silent_voice.jpg', 'rating': 8.9},
        {'title': 'High School DxD', 'year': 2012, 'studio': 'TNK', 'image': 'high_school_dxd.jpg', 'rating': 8.2}
    ],
}

# Create a queue
anime_queue = deque()
prev_anime_stack = deque()

def recommend_anime():
    genre = combo_box.get()
    if not genre:
        recommendation = "Silakan pilih genre anime terlebih dahulu."
        result_label.configure(text=recommendation)
        image_label.configure(image='')
    else:
        anime_queue.clear()
        prev_anime_stack.clear()
        anime_list = anime_genres.get(genre)
        if anime_list:
            for anime in anime_list:
                anime_queue.append(anime)
            show_next_anime()
        # else:
        #     recommendation = "Tidak ada anime yang sesuai dengan Genre."
        #     result_label.configure(text=recommendation)
    
def show_next_anime():
    if anime_queue:
        anime = anime_queue.popleft()
        prev_anime_stack.append(anime)
        title = anime['title']
        year = anime['year']
        studio = anime['studio']
        rating = anime['rating']
        image_filename = anime['image']
        image = ImageTk.PhotoImage(Image.open(image_filename).resize((200, 200)))
        result_label.configure(text=f"Title: {title}\nYear: {year}\nStudio: {studio}\nRating: {rating}")
        image_label.configure(image=image)
        image_label.image = image
    else:
        recommendation = "Tidak ada lagi rekomendasi anime."
        result_label.configure(text=recommendation)
        image_label.configure(image='')
        
def show_previous_anime():
    if prev_anime_stack:
        anime = prev_anime_stack.pop()
        anime_queue.appendleft(anime)
        title = anime['title']
        year = anime['year']
        studio = anime['studio']
        rating = anime['rating']
        image_filename = anime['image']
        image = ImageTk.PhotoImage(Image.open(image_filename).resize((200, 200)))
        result_label.configure(text=f"Title: {title}\nYear: {year}\nStudio: {studio}\nRating: {rating}")
        image_label.configure(image=image)
        image_label.image = image
    else:
        recommendation = "Tidak ada anime sebelumnya."
        result_label.configure(text=recommendation)
        image_label.configure(image='')

# def clear_anime_queue():
#     anime_queue.clear()
#     prev_anime_stack.clear()
#     result_label.configure(text="")
#     image_label.configure(image='')

def clear_combobox_selection():
    combo_box.set("")

# Membuat window
window = tk.Tk()
window.title("Anime Recommendation")

# Set window posisi dan dimensi
window.geometry("1000x800")
window.configure(background='white')

# Set background
background_image = ImageTk.PhotoImage(Image.open("jon.png"))
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Membuat label
label = tk.Label(window, text="Pilih Genre:", font=("Arial", 16), bg='white')
label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

# Membuat combobox
combo_box = ttk.Combobox(window, values=list(anime_genres.keys()), font=("Arial", 14), state='readonly')
combo_box.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

# Membuat button
button = tk.Button(window, text="Rekomendasi Anime", command=recommend_anime, font=("Arial", 12))
button.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

# Membuat label hasil
result_label = tk.Label(window, justify='center', font=("Arial", 12), bg='white', relief='groove')
result_label.grid(row=2, column=5, padx=10, pady=10)

# Membuat label gambar
image_label = tk.Label(window, bg='white')
image_label.grid(row=1, column=5, padx=20, pady=20)

# Mengatur posisi relatif (place) untuk result_label
window.grid_rowconfigure(2, weight=1)
window.grid_columnconfigure(5, weight=1)
result_label.place(relx=0.5, rely=0.67, anchor=tk.CENTER)

# Mengatur posisi relatif (place) untuk image_label
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(5, weight=1)
image_label.place(relx=0.5, rely=0.47, anchor=tk.CENTER)

# Membuat button anime sebelumnya
prev_button = tk.Button(window, text="Anime Sebelumnya", command=show_previous_anime, font=("Arial", 12))
prev_button.place(relx=0.35, rely=0.84, anchor=tk.CENTER)

# Membuat next button
next_button = tk.Button(window, text="Anime Selanjutnya", command=show_next_anime, font=("Arial", 12))
next_button.place(relx=0.65, rely=0.84, anchor=tk.CENTER)

# # Create the clear queue button
# clear_queue_button = tk.Button(window, text="Hapus Anime", command=clear_anime_queue, font=("Arial", 12))
# clear_queue_button.place(relx=0.2, rely=0.94, anchor=tk.CENTER)

# Membuat button hapus genre
clear_selection_button = tk.Button(window, text="Hapus Genre", command=clear_combobox_selection, font=("Arial", 12))
clear_selection_button.place(relx=0.8, rely=0.94, anchor=tk.CENTER)

# Loop window
window.mainloop()
