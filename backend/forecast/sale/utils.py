class ImportUtils:
    def __init__(self, column_headers):
        self.column_headers = column_headers

    def get_column(self, header):
        header = header.strip('\r')
        return self.column_headers.index(header)

    def validate_data(self, data):
        if not data or data == "":
            return None
        else:
            return data.strip()