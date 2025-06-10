import time

def simulate_clock(hours=3):
    total_seconds = hours * 60 * 60
    for sec in range(total_seconds):
        hr = sec // 3600
        min = (sec % 3600) // 60
        s = sec % 60
        print(f"{hr:02} Hour {min:02} Min {s:02} Sec")
        time.sleep(1)

simulate_clock()    