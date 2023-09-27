hesapEce = {
    'Ad':'Ece KAFKAS',
    'Hesap No': 12342345,
    'Bakiye':200.000,
    'Ek hesap':100.000,
}
hesapOmer = {
    'Ad':'Omer KAFKAS',
    'Hesap No':93550155,
    'Bakiye':300.000,
    'Ek Hesap':150.000
}
hesapGoktug = {
    'Ad':'Goktug KAFKAS',
    'Hesap No':20200155,
    'Bakiye':500.000,
    'Ek Hesap':200.000
}

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap ['Ad']},Hosgeldiniz.")
    if (miktar <= hesap["Bakiye"]):
        hesap['Bakiye'] -= miktar
        print('Paranizi alabilirsiniz.')
    else:
        toplam=hesap['Bakiye']+hesap['Ek Hesap']
        if (toplam>=miktar):
            ekHesapKullanimi = input('Ek Hesap Kullanılsın mı e/h:')
            if ekHesapKullanimi=='e':
                ekHesapKullanilacakMiktar = miktar - hesap['Bakiye']
                hesap['Bakiye']=0
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar
                print('Paranizi alabilirsiniz.')
            else:
                print(f"{hesap['Hesap No']} nolu hesabinizda {hesap['Bakiye']} bulunmaktadir.")
        else:
            print("Yetersiz  bakiye!")
def bakiyesorgula(hesap):
    print(f"{hesap['Hesap No']} nolu hesabinizda {hesap['Hesap Bakiye']} TL bulunmaktadir.")

paraCek(hesapGoktug,800.000)
