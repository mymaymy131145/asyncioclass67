import asyncio
import httpx
import time

async def fetch_ability_data(client, url):
    print(f"{time.ctime()} - Fetching data from {url}")
    response = await client.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    data = response.json()
    return data

async def fetch_pokemon_names_with_ability(client, ability_url):
    data = await fetch_ability_data(client, ability_url)
    pokemon_list = data.get('pokemon', [])
    
    # Fetch names of Pokémon asynchronously
    tasks = [fetch_pokemon_name(client, entry['pokemon']['url']) for entry in pokemon_list]
    names = await asyncio.gather(*tasks)
    
    return names

async def fetch_pokemon_name(client, url):
    response = await client.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    data = response.json()
    return data['name']

async def index():
    start_time = time.perf_counter()
    
    async with httpx.AsyncClient() as client:
        # URLs for abilities
        battle_armor_url = 'https://pokeapi.co/api/v2/ability/battle-armor'
        speed_boost_url = 'https://pokeapi.co/api/v2/ability/speed-boost'
        
        # Create tasks to fetch Pokémon names concurrently
        battle_armor_task = fetch_pokemon_names_with_ability(client, battle_armor_url)
        speed_boost_task = fetch_pokemon_names_with_ability(client, speed_boost_url)
        
        # Wait for both tasks to complete
        battle_armor_names = await battle_armor_task
        speed_boost_names = await speed_boost_task
        
        end_time = time.perf_counter()
        
        print(f"{time.ctime()} - Pokémon with 'battle-armor' ability: {', '.join(battle_armor_names)}")
        print(f"{time.ctime()} - Pokémon with 'speed-boost' ability: {', '.join(speed_boost_names)}")
        print(f"Time taken: {end_time-start_time} seconds")

if __name__ == "__main__":
    asyncio.run(index())
