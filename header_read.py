def hdr_read(path):
    row = 0
    col = 0
    bands = 0
    datatype = None
    with open(path, "r") as f:
        for l in f:
            k = l.split()
            if k[0] == "BANDS:":
                 bands = k[1]
            elif k[0] == 'ROWS:':
                row = k[1]
            elif k[0] == 'COLS:':
                col = k[1]
            elif k[0] == 'DATATYPE:':
                datatype = k[1]
    mul, D_type = (255, 'uint8') if datatype == 'U8' else ((2**16-1), 'U16')
    print(mul, D_type)
    return row, col, bands, datatype
