class DataHandler:
    """ main class """
    def __init__(self):
        """ inicializa a classe """
        
        # - input -
        self.in_arquivo = None
        self.in_codec = 'utf8'
        self.total_lines = 0

        # - output -
        self.out_arquivo = None
        self.out_codec = 'utf8'
    
    def input_parameter(self, arquivo, codec):
        """ input """
        self.in_arquivo = arquivo
        self.in_codec = codec
    
    def output_parameter(self, arquivo, codec):
        """ output """
        self.out_arquivo = arquivo
        self.out_codec = codec
