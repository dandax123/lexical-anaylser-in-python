class File:
    def __init__(self,file_name):
        self.file_name = file_name
        try:
            f = open(self.file_name,'r',encoding = 'utf-8')
        except OSError:
            print("Could not access file !!!")
    def read_input_token(self):
        inputs_token = []
        f = open(self.file_name,'r',encoding = 'utf-8')
        for line in f:
            line_data = line.split()
            inputs_token.extend(line_data)
        f.close()
        return inputs_token



