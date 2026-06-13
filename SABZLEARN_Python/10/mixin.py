class PrintInfoMixin:
    def print_info(self):
        print(self.__class__.__name__)
        print(self.__dict__)
        
