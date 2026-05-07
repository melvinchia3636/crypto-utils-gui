def bits_chunk_encode(data, alphabet, bits):
    bitstr = "".join(f"{b:08b}" for b in data)
    result = []

    for i in range(0, len(bitstr), bits):
        chunk = bitstr[i : i + bits].ljust(bits, "0")
        result.append(alphabet[int(chunk, 2)])

    return "".join(result)


def bits_chunk_decode(text, alphabet, bits):
    rev = {}
    for i, entry in enumerate(alphabet):
        if entry not in rev:
            rev[entry] = i

    bitstr = ""
    i = 0
    while i < len(text):
        matched = None
        for entry in rev:
            if text.startswith(entry, i):
                if matched is None or len(entry) > len(matched):
                    matched = entry
        if matched:
            bitstr += f"{rev[matched]:0{bits}b}"
            i += len(matched)
        else:
            i += 1

    result = []

    for i in range(0, len(bitstr) - 7, 8):
        chunk = bitstr[i : i + 8]
        result.append(int(chunk, 2))

    return bytes(result)
