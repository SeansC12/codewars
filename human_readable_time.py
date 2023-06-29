def make_readable(seconds):
    sol = ""
    time = seconds

    hours = int(time / 60 / 60)
    if hours >= 1:
        sol += str(hours).zfill(2)
        time -= hours * 60 * 60
    else:
        sol += "00"
    sol += ":"
    
    minutes = int(time / 60)
    if minutes >= 1:
        sol += str(minutes).zfill(2)
        time -= minutes * 60
    else:
        sol += "00"
    sol += ":"

    sol += str(time).zfill(2)

    return sol

print(make_readable(60))