def format_eta(seconds):
    if seconds < 0:
        return "0s"
    units = [
        ("heat death", "∞", 86400 * 365 * 10**100),
        ("black hole era", "bh", 86400 * 365 * 10**40),
        ("degenerate era", "deg", 86400 * 365 * 10**15),
        ("universe age", "univ", 86400 * 365 * 14 * 10**9),
        ("eon", "eon", 86400 * 365 * 10**9),
        ("epoch", "ep", 86400 * 365 * 10**6),
        ("millennium", "mil", 86400 * 365 * 1000),
        ("century", "c", 86400 * 365 * 100),
        ("decade", "dec", 86400 * 365 * 10),
        ("year", "y", 86400 * 365),
        ("month", "mo", 86400 * 30),
        ("day", "d", 86400),
        ("hour", "h", 3600),
        ("min", "min", 60),
        ("sec", "s", 1),
    ]
    parts = []
    for _, abbr, unit in units:
        if seconds >= unit:
            count = int(seconds / unit)
            seconds -= count * unit
            parts.append(f"{count}{abbr}")
            if unit > 3600 and len(parts) >= 3:
                break
    return " ".join(parts) if parts else "0s"


def format_speed(keys_per_sec):
    if keys_per_sec >= 1_000_000:
        return f"{keys_per_sec / 1_000_000:.1f}M keys/s"
    elif keys_per_sec >= 1_000:
        return f"{keys_per_sec / 1_000:.0f}K keys/s"
    else:
        return f"{keys_per_sec:.0f} keys/s"


ETA_LEGEND = (
    "Time unit legend: ∞=heat death of universe (nothing left in the entire universe) (~10¹⁰⁰ yr), "
    "bh=black hole era (only black holes remain in the universe) (~10⁴⁰ yr), deg=degenerate era (the end of star formation and the dominance of stellar remnants) (~10¹⁵ yr), "
    "univ=universe age (14B yr), eon=10⁹ yr, ep=10⁶ yr, "
    "mil=1000 yr, c=century, y=year, mo=month, d=day, h=hour"
)
