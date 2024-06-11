import httpx
from starlette.requests import Request
from fastapi import APIRouter, HTTPException

from interface.payload import (Payload, Profile)
from interface.response import (UserResults, ItemResults)
from services.predictor import Predict


router = APIRouter()

@router.post("/questions", response_model=UserResults)
async def generate_questions(request: Request, profile: Profile = None) -> UserResults:
    try:
        engine: Predict = request.app.state.engine
        # Read the profile and generate targeted questions using profile
        question_list: UserResults = engine.process_profile(profile)
        return question_list
        
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f"HTTP Error: {str(e)}")
    

@router.post("/answer", response_model=ItemResults)
async def answer_questions(request: Request, question: Payload = None) -> ItemResults:
    try:
        engine: Predict = request.app.state.engine
        # Read the questions and generate answers
        response: ItemResults = engine.process_questions(question)
        return response
        
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f"HTTP Error: {str(e)}")