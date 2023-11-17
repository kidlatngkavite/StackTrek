from threading import Timer
bestFriendName = ""


inputTime = 5
print("who is your bestfriend?")

def displaystring(name):
    """Print a greeting"""
    print(f"Hello, {name}")

inputTimer = Timer(5, lambda: print("\nWriting time is over"))

inputTimer.start()
print("You have 5 seconds to answer", )
bestFriendName = displat
inputTimer.cancel()


