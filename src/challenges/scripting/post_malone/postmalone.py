from fastapi import FastAPI

def read_flag(flag_file="flag"):
    try:
        with open(flag_file, "r") as f:
            return f.read()
    except Exception as e:
        return {"ERROR": "Error reading flag file. Please inform the CTF team!"}

app = FastAPI()

@app.get("/")
async def root():
    return {"error": "The name's POST Malone, not GET Malone!"}

@app.post("/")
async def root():
    return {"flag": read_flag()}
