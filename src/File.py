class File:
    def __init__(self,file_name):
        self.file_name = file_name
        try:
            f = open(self.file_name,'r',encoding = 'utf-8')
        except OSError:
            print("Could not access file !!!")
    def read_input_token(self):
        f = open(self.file_name,'r',encoding = 'utf-8')
        inputs_token = f.readline()
        return inputs_token



