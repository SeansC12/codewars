from collections import defaultdict

def format_duration(seconds):
    if seconds == 0: return "now"
    sol = list()
    time = seconds
    
    years = int(time / 31_536_000)
    if years >= 1:
        time -= years * 31_536_000
    else:
        years = 0
    
    days = int(time / 86400)
    if days >= 1:
        time -= days * 86400
    else:
        days = 0
    
    hours = int(time / 3600)
    if hours >= 1:
        time -= hours * 3600
    else:
        hours = 0
    
    minutes = int(time / 60)
    if minutes >= 1:
        time -= minutes * 60
    else:
        minutes = 0
    
    seconds = time

    years_dict = defaultdict(lambda: f"{years} years", {0: "", 1: f"{years} year"})
    days_dict = defaultdict(lambda: f"{days} days", {0: "", 1: f"{days} day"})
    hours_dict = defaultdict(lambda: f"{hours} hours", {0: "", 1: f"{hours} hour"})
    minutes_dict = defaultdict(lambda: f"{minutes} minutes", {0: "", 1: f"{minutes} minute"})
    seconds_dict = defaultdict(lambda: f"{seconds} seconds", {0: "", 1: f"{seconds} second"})

    sol.extend([years_dict[years], days_dict[days], hours_dict[hours], minutes_dict[minutes], seconds_dict[seconds]])
    sol = list(filter(lambda x: not x == "", sol))
    
    if len(sol) > 1:
        last_elem = sol.pop()
        return ", ".join(sol) + " and " + last_elem
    
    
    return "".join(sol)

print(format_duration(3662))