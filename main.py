import random

yashirin = random.randint(1, 100)
maks_urinish = 7

for i in range(maks_urinish):
    taxmin = int(input("Sonni top (1-100): "))

    if taxmin == yashirin:
        print("🎉 Yutdingiz!")
        break
    elif taxmin < yashirin:
        print("⬆️ Kattaroq son")
    else:
        print("⬇️ Kichikroq son")

else:
    print("❌ Yutqazdingiz. Son:", yashirin)
