import requests
import random
import webbrowser
import io
import time
from tkinter import*
from PIL import Image
from PIL import ImageTk
from urllib.request import urlopen
from io import BytesIO

"""

    print(pokemon['name'])
    print(pokemon['sprites']['front_default'])

    webbrowser.register('chrome', 
                        None, 
                        webbrowser.BackgroundBrowser("C://Users//Vues//AppData//Local//Google//Chrome//Application//chrome.exe"))
    webbrowser.get('chrome').open(pokemonImage)
"""


pokemon_API = 'https://pokeapi.co/api/v2/pokemon/'

def newPokemon():

    pokemonNumber = random.randint(1,151)
    convertedNum = str(pokemonNumber)

    pokemonURL_NUMBER = pokemon_API + convertedNum

    pokemon = requests.get(pokemonURL_NUMBER).json()
    pokemonImage = pokemon['sprites']['front_default']
    pokemonName = pokemon['name'].capitalize() 

    myPokemonName = Label(canvas1, text=pokemonName)
    myPokemonName.pack(pady=20)

    response = requests.get(pokemonImage)
    img_data = response.content
    img = ImageTk.PhotoImage(Image.open(io.BytesIO(img_data)))
    panel = Label(canvas1, image=img)
    panel.image = img
    panel.pack(padx=100, pady=10)
    canvas1.after(1000, panel.destroy)
    canvas1.after(1000, myPokemonName.destroy)
    canvas1.after(1000, newPokemon)


def newShiny():


    pokemonNumber = random.randint(1,151)
    convertedNum = str(pokemonNumber)

    pokemonURL_NUMBER = pokemon_API + convertedNum

    pokemon = requests.get(pokemonURL_NUMBER).json()
    pokemonImage = pokemon['sprites']['front_shiny']
    pokemonName = pokemon['name'].capitalize() 

    myPokemonName = Label(canvas1, text=pokemonName)
    myPokemonName.pack(pady=20)

    response = requests.get(pokemonImage)
    img_data = response.content
    img = ImageTk.PhotoImage(Image.open(io.BytesIO(img_data)))
    panel = Label(canvas1, image=img)
    panel.image = img
    panel.pack(padx=100, pady=10)
    canvas1.after(1000, panel.destroy)
    canvas1.after(1000, myPokemonName.destroy)
    canvas1.after(1000, newShiny)
    


root = Tk()
root.eval('tk::PlaceWindow . center')

myButton = Button(root, text="Spawn Pokemon", 
                        width=20, 
                        command=lambda:newPokemon())
myButton.pack()

shinyButton = Button(root, text="Spawn Shiny", 
                            width=20,
                            command=lambda:newShiny())
shinyButton.pack()

exitButton = Button(root, text="Close", 
                        width=20, 
                        command=root.destroy)
exitButton.pack()

canvas1 = Canvas(root, width=300, height=200)
canvas1.pack()

root.title("Pokemon Slideshow")
root.mainloop()