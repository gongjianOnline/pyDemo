

__all__ = ["myAdd"]

def myAdd(a,b):
    print(a+b)
    print(__name__)


# 范式
if __name__ == "__main__":
    myAdd(1,2)