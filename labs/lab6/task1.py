TimeUnits = {
    "s": 1,
    "m": 60,
    "h": 3600,
    "d": 86400
}

def ConvertTime(time_str, target_unit):
    for unit in TimeUnits:
        if time_str.endswith(unit):
            value = int(time_str[:-len(unit)])
            seconds = value * TimeUnits[unit]
            result = seconds / TimeUnits[target_unit]
            return f"{int(result)}{target_unit}"
    return "Error!"

inp = input().split()
print(ConvertTime(inp[0], inp[1]))