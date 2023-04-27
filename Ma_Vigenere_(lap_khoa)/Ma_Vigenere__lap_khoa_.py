
# Ma Vigenere _ lap khoa

def nhapSoNguyen(mes,min,max):
    while True:
        a = input(mes).strip() # strip de xoa khoang trang, tuong tu trim()
        try:
            a = int(a)
            if a>max or a<min:
                print('Ban phải chon gia tri trong [',min,',',max,'].')
            else: return a
        except ValueError:
            print('Loi... Hay nhap dung yeu cau!')
            
def showMenu():
    print('Chon 1 trong cac chuc nang sau:')
    print('1. Ma hoa')
    print('2. Giai ma')
    print('0. Thoat')
    luaChon = nhapSoNguyen("Lua chon cua ban la: ",0,2)
    return luaChon

# Lay chi so cua 1 chu cai trong bang chu cai
def get_index(chu_cai, bangchucai):
    for i in range(len(bangchucai)):
        if bangchucai[i] == chu_cai:
            return i

def ma_hoa(chu_cai_ro, chu_cai_khoa, bangchucai):   # Ma hoa chi 1 chu cai
    index_ban_ro = get_index(chu_cai_ro, bangchucai)
    index_khoa = get_index(chu_cai_khoa, bangchucai)
    index_ban_ma = (index_ban_ro + index_khoa) % 26
    return bangchucai[index_ban_ma]

def giai_ma(chu_cai_ma, chu_cai_khoa, bangchucai):   # Giai ma chi 1 chu cai
    index_ban_ma = get_index(chu_cai_ma, bangchucai)
    index_khoa = get_index(chu_cai_khoa, bangchucai)
    index_ban_ro = (index_ban_ma - index_khoa) % 26
    return bangchucai[index_ban_ro]

if __name__ == "__main__":
    bangchucai = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    while True:
        luaChon = showMenu()
        if luaChon == 0:    # Thoat
            print('Bye...')
            break
        elif luaChon == 1:  # Ma hoa
            print('Chuc nang 1. Ma hoa')
            ban_ro = input('Nhap ban ro: ').strip().upper()
            khoa = input('Nhap khoa: ').strip().upper()
            # Ma hoa
            ban_ma = ''
            for i in range(len(ban_ro)):
                ban_ma += ma_hoa(ban_ro[i], khoa[i%len(khoa)], bangchucai) 
            print('Ban ma cua',ban_ro,'la:',ban_ma) 
            if input("Nhap bat ki de tiep tuc, nhap 'x' de thoat: ").strip().upper() == 'X':
                print('Bye...')
                break
        else:   # Giai ma
            print('Chuc nang 2. Giai ma')
            ban_ma = input('Nhap ban ma: ').strip().upper()
            khoa = input('Nhap khoa: ').strip().upper()
            # Giai ma
            ban_ro = ''
            for i in range(len(ban_ma)):
                ban_ro += giai_ma(ban_ma[i], khoa[i%len(khoa)], bangchucai) 
            print('Ban ma cua',ban_ma,'la:',ban_ro) 
            if input("Nhap bat ki de tiep tuc, nhap 'x' de thoat: ").strip().upper() == 'X':
                print('Bye...')
                break
