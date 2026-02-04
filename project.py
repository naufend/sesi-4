current_room = "perpustakaan"
inventory = []

print("=== Mini Text Adventure Game ===")
print("Tujuan: Temukan kunci dan buka pintu untuk menang!")

while True:
    print("\nKamu berada di:", current_room)
    print("Command yang tersedia:")

    if current_room == "perpustakaan":
        print("1. get key")
        print("2. go south")
        print("3. quit")
    elif current_room == "koridor":
        print("1. unlock door")
        print("2. go north")
        print("3. quit")

    command = input("Masukkan perintah: ").lower()

    # RUANGAN 1: PERPUSTAKAAN
    if current_room == "perpustakaan":
        if command == "get key":
            if "key" not in inventory:
                inventory.append("key")
                print("Kamu mendapatkan kunci 🔑")
            else:
                print("Kamu sudah punya kunci.")
        elif command == "go south":
            current_room = "koridor"
            print("Kamu masuk ke koridor.")
        elif command == "quit":
            print("Terima kasih sudah bermain!")
            break
        else:
            print("Perintah tidak valid. Pilih dari daftar command.")

    elif current_room == "koridor":
        if command == "unlock door":
            if "key" in inventory:
                print("Kamu membuka pintu dan MENANG! 🎉")
                break
            else:
                print("Pintu terkunci. Kamu butuh kunci.")
        elif command == "go north":
            current_room = "perpustakaan"
            print("Kamu kembali ke perpustakaan.")
        elif command == "quit":
            print("Terima kasih sudah bermain!")
            break
        else:
            print("Perintah tidak valid. Pilih dari daftar command.")
