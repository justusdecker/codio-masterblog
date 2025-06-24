from json import load, dumps

def jff(path: str) -> list | dict:
    """ returns a json file """
    with open(path,'r') as f_in:
        return load(f_in)

def jsf(path: str, data: dict | list) -> None:
    """ write json to a file """
    with open(path,'w') as f_out:
        f_out.write(dumps(data,indent=2))