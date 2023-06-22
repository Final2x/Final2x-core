def singleton(cls):
    instances = {}

    def getinstance(*args, **kw):
        if cls not in instances:
            if isinstance(cls, type):
                instances[cls] = cls(*args, **kw)
            else:
                instances[cls] = cls
        else:
            print("class already exists")
        return instances[cls]

    if isinstance(cls, type):
        return getinstance
    else:
        return getinstance(cls)
