import httpx
import asyncio
from random import randint, choice
from datetime import datetime

BASE_URL = "http://localhost:8000"

usernames = ["s1mple", "NiKo", "ZywOo", "device", "sh1ro",
             "electronic", "b1t", "Boombl4", "Perfecto", "Jame"]
maps = ["de_dust2", "de_mirage", "de_inferno", "de_nuke", "de_overpass"] * 20


async def seed():
    async with httpx.AsyncClient() as client:
        player_ids = []
        for i, username in enumerate(usernames):
            response = await client.post(f"{BASE_URL}/player", json={"username": username,
                                                                     "email": f"{username}@gmail.com"})
            player_ids.append(response.json()["id"])

        match_ids = []
        for map_name in maps:
            match_response = await client.post(f"{BASE_URL}/match", json={
                "map_name": map_name,
                "played_at": datetime.now().isoformat(),
                "duration_seconds": randint(600, 2700)
            })
            match_ids.append(match_response.json()["id"])

        for match_id in match_ids:
            for player_id in player_ids:
                await client.post(f"{BASE_URL}/match_result", json={
                    "player_id": player_id,
                    "match_id": match_id,
                    "kills": randint(0, 35),
                    "deaths": randint(0, 35),
                    "assists": randint(0, 10),
                    "winner": choice([True, False])
                })


asyncio.run(seed())
