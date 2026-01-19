import itertools, time
from hashing import hash_password

def dictionary_attack(target, algo, salt, words, limiter, stop_flag):
    attempts = 0
    for w in words:
        if stop_flag(): break
        if not limiter.allow(): time.sleep(0.01)

        w = w.strip()
        attempts += 1
        if hash_password(w, algo, salt) == target:
            return w, attempts
    return None, attempts


def brute_force_attack(target, algo, salt, charset, max_len, limiter, stop_flag):
    attempts = 0
    start_time = time.time()

    for length in range(1, max_len + 1):
        for combo in itertools.product(charset, repeat=length):
            if stop_flag():
                return None, attempts

            if not limiter.allow():
                time.sleep(0.01)

            attempts += 1
            pwd = "".join(combo)
            if hash_password(pwd, algo, salt) == target:
                return pwd, attempts

    return None, attempts
