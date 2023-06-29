def is_pangram(s):
    return True if set(s.lower()) >= set("abcdefghijklmnopqrstuvwxyz") else False