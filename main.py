from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, Response
from pydantic import BaseModel, ConfigDict


app = FastAPI(
    title="Task API",
    version="1.0",
    description="A simple in-memory Task Management API built with FastAPI.",
)

