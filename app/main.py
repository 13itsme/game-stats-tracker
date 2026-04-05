from fastapi import FastAPI
from app.api.v1.players import router as player_router
from app.api.v1.matches import router as matches_router
from app.api.v1.match_results import router as match_results_router


app = FastAPI()

app.include_router(player_router)
app.include_router(matches_router)
app.include_router(match_results_router)
