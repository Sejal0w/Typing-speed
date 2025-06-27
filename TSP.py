import time
sentence = "Python is fun and powerful."
print("Type the following:")
print(sentence)
input("Press Enter to start...")
start = time.time()
typed = input("Type: ")
end = time.time()

duration = round(end - start, 2)
speed = round((len(typed.split()) / duration) * 60, 2)
print(f"Time: {duration} sec | Speed: {speed} WPM")
