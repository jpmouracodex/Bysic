import basic

while True:
    text = input("> ")
    
    result, error = basic.run(text)
    
    if error: print(error)
    else: print(result)
