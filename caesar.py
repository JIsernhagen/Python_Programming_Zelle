def main():
    action, phrase, key = input("Please input action (encode/decode), phrase and key:  ")
    processed = ''
    for ch in phrase:
        processed = processed + chr(ord(ch)+key)
    print("Processed output: ".format(coded))

main()