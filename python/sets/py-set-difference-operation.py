_ = int(input())
english_rol = set(input().split())
_ = int(input())
french_rol = set(input().split())
print(len(english_rol.difference(french_rol)))

