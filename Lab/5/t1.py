with open("file.txt",'r') as fileObj:
    #fileObj.write("Ek dafa ek banda FAST mey agea pher...")
    try:
        content = fileObj.read()
        print (content)
        totalChar = len(content)
        totalWords = len(content.split())
        print (f"Total words is: {totalWords}\nTotal Chars: {totalChar}  \n")
        x =0 
        for x, content in enumerate (content, start=1):
            pass
        print("By counter: total chars: ",x)
    
    except FileNotFoundError:
        print("file not found!")