import requests
from bs4 import BeautifulSoup
import json

"""
2. Gunakan API dari PokeAPI
https://pokeapi.co/

Input:
Masukkan Nama Pokemon :

Output:
- Nama Pokemon :
- HP :
- Attack :
- Defense :
- Speed :
- Type :
- Image : (URL Image)
- Ability Pokemon :
   1.
   2.
   3.
"""

try:
    q = str(input("Masukkan Nama Pokemon : "))
    halo = q.lower()  
    hai = halo.replace(" ","-")
    url = "https://pokeapi.co/api/v2/pokemon/"+hai
    data = requests.get(url)
    poke = data.json()
    # print(poke)

    namapokemon = poke['species']['name']
    hp = poke['stats'][0]['base_stat']
    attack = poke['stats'][1]['base_stat']
    defense = poke['stats'][2]['base_stat']
    spattack = poke['stats'][3]['base_stat']
    spdefense = poke['stats'][4]['base_stat']
    speed = poke['stats'][5]['base_stat']
    panjangtype = len(poke['types'])
    fotopokemon = poke['sprites']['front_default']

    type2 = ""
    if panjangtype == 1:
        type1 = poke['types'][0]['type']['name']
    elif panjangtype == 2:
        type1 = poke['types'][0]['type']['name'] + ","
        type2 = poke['types'][1]['type']['name']
        
    # print(poke['types'])

    print("• Nama Pokemon :", namapokemon.title())
    print("• HP :", hp)
    print("• Attack :", attack)
    print("• Defense :", defense)
    print("• Sp. Attack :", spattack)
    print("• Sp. Defense :", spdefense)
    print("• Speed :", speed)
    print("• Type :", type1.title(), type2.title())
    print("• Image :", fotopokemon)
    print("• Ability Pokemon :",)
    # print(poke['abilities'])

    for i in poke['abilities']:
        print("  -", i['ability']['name'].title())
except:
    print("Nama Pokemon yang anda masukkan tidak ditemukan !")

