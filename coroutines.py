import re
# coroutine defintiions
def coroutine(regex):
    # coroutine logic is executed when __next__() method is called
    print("Coroutine is started!")
    try:
        while True:
            print("Waiting for data!")
            # suspends coroutine until data is provided through send() method
            txt=(yield)
            # coroutine execution is continued
            print("Received data!")

            result=re.search(regex,txt)
            if(result is not None):
                print(result.group())
    # calling close() method results in throwing GeneratorExit exception
    except GeneratorExit as exc:
        print("Coroutine is closed!")

def main():
    ref=coroutine("\d")
    print("Calling coroutine __next__ method!")
    ref.__next__()
    print("Sending data to coroutine!")
    ref.send("Today is 8th of May!")
    print("Sending data to coroutine!")
    ref.send("Hello world!")
    print("Closing coroutine!")
    ref.close()



if __name__=="__main__":
    main()