from fastapi import FastAPI

# Create the FastAPI app
app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI!"}

# Simple dynamic route
@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}

# Add two numbers using query parameters
@app.get("/add")
def add_numbers(a: int, b: int):
    return {"result": a + b}

# Run the API if executed directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

