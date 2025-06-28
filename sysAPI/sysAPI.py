from fastapi import FastAPI, Query
import os
import asyncio
import uvicorn
import subprocess
from fastapi.responses import RedirectResponse
import json
import shlex

app = FastAPI()


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
async def uptime():
    result = subprocess.run(["uptime"], stdout=subprocess.PIPE)
    return {"uptime": result}


@app.get("/ping")
async def ping(url: str = Query(...)):
    try:
        result = subprocess.run(
            ["ping", "-c", "4", url],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        return {
            "success": result.returncode == 0,
            "stdout": result.stdout,
            "stderr": result.stderr,
        }
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
