from preloaded import MORSE_CODE as MC


def decode_morse(m_code):
    message = "".join([MC[i] if i in MC else " " for i in m_code.split(" ")])
    return message.replace("  ", " ").strip()

# MC = {".-":  "A", "-...": "B", "-.-.": "C", "-..":  "D",
#       ".":   "E", "..-.": "F", "--.":  "G", "....": "H",
#       "..":  "I", ".---": "J", "-.-":  "K", ".-..": "L",
#       "--":  "M", "-.":   "N", "---":  "O", ".--.": "P",
#       "--.-":"Q", ".-.":  "R", "...":  "S", "-":    "T",
#       "..-": "U", "...-": "V", ".--":  "W", "-..-": "X",
#       "-.--":"Y", "--..": "Z", "...---..."  :   "SOS",
#       ".----":"1", "..---":"2","...--":"3","....-":"4",".....":"5",
#       "-....":"6","--...":"7","---..":"8","----.":"9","-----":"0",
#       "...-..-":"$", }
#
#
# def decode_morse(morse_code):
#     morse_code += " "
#     # morse_code = morse_code.split()
#     word = morse_code[0]
#     for i in range(1, len(morse_code)):
#         if morse_code[i] == " ":
#             print(MC[word])
#             word = ""
#             if morse_code[i - 1] == " ":
#                 print(" ", end="")
#         else:
#             word += morse_code[i]
#     return 0


decode_morse("--...")
decode_morse(".")
decode_morse("-")
decode_morse("...-")
