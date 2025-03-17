def get_aprs_pw(callsign: str):
    cs = callsign.upper()
    i = 0
    tmp_code = 29666

    while i < len(cs):
        tmp_code = tmp_code ^ ord(cs[i]) * 256
        try:
            tmp_code = tmp_code ^ ord(cs[i + 1])
        except IndexError:
            pass
        i += 2
    tmp_code = tmp_code & 32767
    return tmp_code
