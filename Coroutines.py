def searcher():
    import time
    #some book i am reading or doing work which takes some time like here 4 seconds
    book = "This is a book on harry and code with harry and good"
    time.sleep(4) #this delay is for the searcher function to work

    while True:
        text = (yield)
        if text in book:
            print("Your text is in the book")
        else: print("Text is not in the book")

search = searcher()
next(search)
search.send("harry")
input("press any key: ")
search.send("harry and") #from second time the searcher takes very less time than first one which sleeps for 4 seconds 
input("press any key: ")
search.send("joker")
search.close #use this when you don't want to use it again cause you need to again run it otherwise it will give error