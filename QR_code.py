import segno
qrcode = segno.make('Yellow Submarine', version=7, error='h')
qrcode.save('qrcode_yellow-submarine.png', scale=4, dark='darkred',
            data_dark='darkorange', data_light='yellow')
