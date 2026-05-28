class Rectangel:
    def __init__(self, arz: int, tool: int) -> None:
        self.arz = arz
        self.tool = tool
    
    def mohit(self, tool: int , arz: int):
        return f'Mohit : {(tool + arz) * 2}'
    
    def masahat(self, tool: int , arz: int):
        return f'Masahat : {tool * arz}'