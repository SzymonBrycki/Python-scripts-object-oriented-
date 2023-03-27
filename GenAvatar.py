import python_avatars as pa 

class GenAvatar():
    def szymons(self):
        my_avatar = pa.Avatar(
            style = pa.AvatarStyle.CIRCLE,
            background_color = "#6FBF0D",
            top = pa.HairType.WILD,
            eyebrows = pa.EyebrowType.DEFAULT_NATURAL,
            eyes = pa.EyeType.HAPPY,
            nose = pa.NoseType.DEFAULT,
            mouth = pa.MouthType.SMILE,
            # facial_hair = pa.FacialHairType.BEARD_LIGHT,
            # You can use hex colors on any color attribute...
            skin_color = pa.SkinColor.LIGHT,
            # Or you can use the colors provided by the library
            hair_color = pa.HairColor.BROWN_DARK,
            accessory = pa.AccessoryType.ROUND,
            clothing = pa.ClothingType.COLLAR_SWEATER,
            clothing_color = pa.ClothingColor.BLUE_02
            )

        my_avatar.render("my_avatar.svg")

    def random(self):
        random_avatar = pa.Avatar.random()
        random_avatar.render("random_avatar.svg")

if __name__ == "__main__":
    oAvatar = GenAvatar()
    oAvatar.szymons()
    print("Generating avatar finished!")