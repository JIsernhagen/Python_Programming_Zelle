def main():
    action, phrase, key = input("Please input action (encode/decode), phrase and key:  ").split(",")
    phrase = phrase.strip()
    key = int(key.strip())
    action = action.strip()
    processed = ''
    if action == 'encode':
        for ch in phrase:
            processed = processed + chr(ord(ch) + key)
    else:
        for ch in phrase:
            processed = processed + chr(ord(ch) - key)
    print("Processed output: {0}".format(processed))
main()