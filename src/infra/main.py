import uvicorn

from src.infra.app import app
from src.utils.env import PORT


def main():
    uvicorn.run(app, host="0.0.0.0", port=PORT)


def dev():
    uvicorn.run("infra.main:app", host="0.0.0.0", port=3000, reload=True)


if __name__ == "__main__":
    main()
