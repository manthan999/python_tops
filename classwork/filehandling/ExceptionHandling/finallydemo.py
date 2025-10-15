
def test():
    try:
        a  = int(input("enter number : "))
        return 1
    except Exception as e:
        # print(e)
        return 0
    finally :
      print("test function called...")

k=test()
print(k)