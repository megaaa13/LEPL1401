def fine(authorized_speed: int, actual_speed: int):
    g = actual_speed - authorized_speed
    if g <= 0: return 0
    if g * 5 < 12.5: return 12.5
    return g * 5 * 2 if g > 10 else g * 5