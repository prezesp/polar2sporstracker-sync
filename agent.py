from app import App
from PyIOKitMatchingHandler import IOKitMatchingHandler

handler = IOKitMatchingHandler()
handler.handle()
app = App()
app.run()
