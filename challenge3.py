secret = "python"

while True:
    tebakan = input("Tebak kata rahasianya: ")

    if tebakan == secret:
        print("Kamu benar!")
        break
    else:
        print("Salah, coba lagi.")
