def main():
    action, phrase, key = input("Please input action (encode/decode), phrase and key:  ").split(",")
    phrase = phrase.strip()
        #.lower()
    key = int(key.strip())
    action = action.strip()
    alphabet = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    processed = ''
    if action == 'encode':
        for ch in phrase:
            p = alphabet.find(ch)
            newposition = p + key
            if newposition > 52:
                newposition = newposition - 53
            processed = processed + alphabet[newposition]
    else:
        for ch in phrase:
            p = alphabet.find(ch)
            newposition = p - key
            if newposition < 0:
                newposition = newposition + 53
            processed = processed + alphabet[newposition]
    print("Processed output: {0}".format(processed))

main()