from uvicorn import run

from configs\
    import APP

from routes\
    import setupRoutes

def main():
    setupRoutes()

    run(
        app=APP,
        host="127.0.0.1",
        port=8000,
    )

if __name__ == "__main__": main()