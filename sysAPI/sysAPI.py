from fastapi import FastAPI, Query
import os
import asyncio
import uvicorn
import subprocess
from pydantic import BaseModel
from typing import List, Optional
from fastapi.responses import RedirectResponse
import json
import shlex

app = FastAPI()

class PingResponse(BaseModel):
    success: bool
    stdout: str
    stderr: str
    
class RunResponse(BaseModel):
    stdout: str
    stdin: str
    
class Uptime(BaseModel):
    uptime : str
    
@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")

@app.get("/system")
async def system():
    stream = os.popen("fastfetch --format json")
    return json.loads(stream.read())


@app.get("/system/cpu")
async def cpu():
    result = subprocess.run(["lscpu", "-J"], stdout=subprocess.PIPE, text=True)
    cpu_info = json.loads(result.stdout)
    return cpu_info


@app.get("/system/uptime")
async def uptime() -> Uptime:
    proc = await asyncio.create_subprocess_exec(
        "uptime",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    
    if stderr:
        raise RuntimeError(f"Error retrieving uptime: {stderr.decode().strip()}")

    return Uptime(uptime=stdout.decode().strip())


@app.get("/ping")
async def ping(url: str = Query(...)) -> PingResponse:
    try:
        result = subprocess.run(
            ["ping", "-c", "4", url],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        return PingResponse(
            success=result.returncode == 0,
            stdout=result.stdout,
            stderr=result.stderr,
        )
    except Exception as e:
        return {"error": str(e)}


@app.get("/run")
async def run(command: str = Query(...)):
    try:
        cmd_parts = shlex.split(command)
        if not cmd_parts:
            return {"error": "Empty command"}
        
        result = subprocess.run(
            cmd_parts,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        return {
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip()
        }

    except Exception as e:
        return {"error": str(e)}



if __name__ == "__main__":
    uvicorn.run("sysAPI:app", host="127.0.0.1", port=8000, reload=True)
