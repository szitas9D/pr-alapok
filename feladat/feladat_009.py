#feladat_009
sebesség = input("Kérek egy sebességet")
sebesség = int(sebesség)
if sebesség <= 50:
    print("A megengedett sebeséggel hajtottál")
elif sebesség <= 0:
    print("Megálltál")
elif 50 < sebesség <= 65:
    print("Gyorshajtást tettél 15.000FT a büntetésed")
elif 65 < sebesség <= 80:
    print("Gyorshajtást tettél 30.000FT a büntetésed")
elif 80 < sebesség <= 100:
    print("Gyorshajtást tettél 60.000FT a büntetésed")