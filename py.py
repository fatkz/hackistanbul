import base64
code = "MTI0MDE3MzAxNzQwMTUxMDE0OTAxNTEwMTUwMDE0NjAxNzkwMTQ5MDExMTcwMTQ2MDE4NTAxMTA1MDE2NjAxMTE3MDE0NjAxMTA1MDE2NjAxODMwMTY5MDExMjY="
decimal = base64.b64decode(code).decode().split("01")
for d in decimal:
    print(chr(int(d)-1), end="")
print()