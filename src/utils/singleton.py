def singleton(cls):
    instances = {}

    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        else:
            print("class already exists")
        return instances[cls]

    if isinstance(cls, type):
        return getinstance
    else:
        return getinstance(cls)
