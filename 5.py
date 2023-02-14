def fa(asci=32, a=" "):
    if asci >= 128:
        return 0

    def ptt(asci):
        a = f"| {asci} = {chr(asci)}"
        return a
    print(f"| {ptt(asci)} | {ptt(asci+1)} | {ptt(asci+2)} | {ptt(asci+3)} | {ptt(asci+4)} | {ptt(asci+5)} | {ptt(asci+6)} | {ptt(asci+7)} | {ptt(asci+8)} | {ptt(asci+9)} |")

    return fa(asci+10)


fa()
