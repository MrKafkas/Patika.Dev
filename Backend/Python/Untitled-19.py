bookNum=input("Kitap Kodunu Giriniz:")
book1 = {
    'name':'Calikusu',
    'writer':'Resat Nuri Guntekin',
    'category':'Roman',
    'release date':'1922'
    }
book2 = {
    'name':'Küçük Prens',
    'writer':'Antoine de Saint-Exupéry',
    'category':'Masal',
    'release date':'1943'
    }

book3 = {
    'name':'Yüzbaşının Kızı',
    'writer':'Puşkin',
    'category':'Roman',
    'release date':'1836'
    }

def kitapBul(**bookNum):
    print(**bookNum)

kitapBul(bookNum)