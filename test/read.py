
def func():
  fname = input("Enter the name of the file you wish to open for reading: ")

  try:
    musicList = []
    f = open(fname)


    musicList = [line.rstrip('\n') for line in f]

    print(musicList)
  except:
    print("Error: reading from the file")
  finally:
    f.close() # close the file


func()

