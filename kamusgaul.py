meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "BTW": "By The Way",
            "OMW": "On My Way, Dalam Perjalanan",
            "GG": "Good Game",
            }

word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")

if word in meme_dict.keys():
    #Apa yang harus kita lakukan jika kata itu ditemukan?
    print(meme_dict[word])
    
else:
    #Apa yang harus kita lakukan jika kata itu tidak ditemukan?
    print("Mohon Maaf Kata Tersebut Tidak Ada Di Kamus")
