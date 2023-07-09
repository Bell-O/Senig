import random
import base64
from colorama import Fore
import os, sys, base64, subprocess, platform
import pyfiglet


def clear():
    if platform.system() == "Windows":
        subprocess.Popen("cls",
                         shell=True).communicate()
    else:  # Linux and Mac
        print("\033c", end="")

def enigma_encode(message, rotors, alphabet):
    encoded_message = ""
    
    for char in message:
        if char.isalpha():
            char = char.upper()
            position = alphabet.index(char)
            
            for rotor in rotors:
                position = rotor.index(alphabet[position])
                
            encoded_message += alphabet[position]
        else:
            encoded_message += char
    
    return encoded_message

def pin_enigma_encode(encoded_message, rotors, alphabet, pin):
    pin_encoded_message = encoded_message
    
    for _ in range(int(pin)):
        encoded_message = ""
        for char in pin_encoded_message:
            if char.isalpha():
                char = char.upper()
                position = alphabet.index(char)

                for rotor in rotors:
                    position = rotor.index(alphabet[position])

                encoded_message += alphabet[position]
            else:
                encoded_message += char
        
        pin_encoded_message = encoded_message
    
    return pin_encoded_message

def enigma_decode(message, rotors, alphabet):
    decoded_message = ""
    
    for char in message:
        if char.isalpha():
            char = char.upper()
            position = alphabet.index(char)
            
            for rotor in reversed(rotors):
                position = alphabet.index(rotor[position])
                
            decoded_message += alphabet[position]
        else:
            decoded_message += char
    
    return decoded_message

def pin_enigma_decode(encoded_message, rotors, alphabet, pin):
    pin_decoded_message = encoded_message
    
    for _ in range(int(pin)):
        decoded_message = ""
        for char in pin_decoded_message:
            if char.isalpha():
                char = char.upper()
                position = alphabet.index(char)

                for rotor in reversed(rotors):
                    position = alphabet.index(rotor[position])

                decoded_message += alphabet[position]
            else:
                decoded_message += char
        
        pin_decoded_message = decoded_message
    
    return pin_decoded_message

def encode_base64(message):
    encoded_message = base64.b64encode(message.encode()).decode()
    return encoded_message

def decode_base64(encoded_message):
    decoded_message = base64.b64decode(encoded_message).decode()
    return decoded_message

# สร้าง rotors
rotors = [
list("QWISHMFDLJVEUYZTPCROGNAXBK"),
    list("PHOSGKJEUDVNYQCTIMABZWFLXR"),
    list("ZYKFJXBNIWRSACDOMULQGVHPTE"),
    list("GHNOUZMVYLQWSFXARKEJTCBPDI"),
    list("RPUHOSVMZEQTFDBGLWAKNXCIYJ"),
    list("ZNXSKHJPATEQVOGDCRIYLWBMUF"),
    list("HMEBDLXJRQSUIZFNVTWAGCPKOY"),
    list("EYHKDVJNSAULBCRGOWZIQPFTXM"),
    list("IYPDTSMRLZCOEAHNFJBGKQXVUW"),
    list("YUPWTZCRVLSEONBQHMAJFKXDIG"),
    list("KEGTWXFACMSYBQONZRHVIJUDLP"),
    list("CXIVQWPKNOJUHLFTZGSEDYMBAR"),
    list("IVHKEPGMAYTRWDJSNZCUFQLBOX"),
    list("MIOZJRYGTSUCNVQKDWXLHBAFEP"),
    list("VYCBXHOMEAFTPQUDNILWGRSJKZ"),
    list("NVYXILAKTJZOEFWCGRBHDQUPSM"),
    list("AQTFCEYRINGWKBLXMDHVZPSOJU"),
    list("BYDSROCWAEIGKQVJMLXTUNHZPF"),
    list("GEFLPMDYWRCOKSUBNJIXQVATZH"),
    list("SGNUAIEQHVBKYFDWRCJLZTXMOP"),
    list("XHISGMTCLAJWNKVBFYRQODUZEP"),
    list("LYCHVUOFWDRKNISEBMZPTAJXQG"),
    list("IFWOSLXNRBUDCZEPMVTJYAKGQH"),
    list("XGVQFPEDBCZUAJLWKMSRTNOHYI"),
    list("YHXVECBMKWFRJZPITSDUAGNLQO"),
    list("XJZVEGUHQBPKRTDMOFCISWAYLN"),
    list("TCBKADOJGVEMYIXZUWPNQRSHLF"),
    list("BXECVAPGHTZKFSNWQMIYJLUROD"),
    list("QDFUXIAJWPSGMZKYNHECBRLVTO"),
    list("NMOJAYVHFEIUQGDZKWBCSXRPLT"),
    list("GFDYTOZMKVPLIECWUSXNRHJBQA"),
    list("SIJMZYFVPDHGBCWRNXKLTEAUOQ"),
    list("XEOUJCRMLFSAIBWDPKTYVHQZGN"),
    list("NGQRDYAJSTEPZCOIFMLKUXHWBV"),
    list("VWHRQTPLBFDYOZMKNEXAGSCUIJ"),
    list("VHYSLGPCNXMOWZAIEJDUTRFQKB"),
    list("ETNDBRJWOULVYZIAPSFGXHCKQM"),
    list("XNABSDPHJGFCZWYVRQEOULTIMK"),
    list("NHRZOIEMSXFBLQGTUPCWDAVKYJ"),
    list("UFBXYJZWTHLRAIEOCQVNSMPDGK"),
    list("SYETWICNUZALPJHKGQBFVMDXOR"),
    list("LDNWQREHUAPBJICKSOFYGTMVZX"),
    list("CTFRAKUIPOQBWDXVZLHNGMSEJY"),
    list("OGJETNYBPXRLSMVAZICUFWDKHQ"),
    list("USPWTVCINQRGZHELYJKDBMXAFO"),
    list("TUVXCWHMBOEFAQNGJIKLSYZPRD"),
    list("EFLCBWJKSXINZMTGQRDAOYHUVP"),
    list("AECHTDQOYLRUFKZSVNGXIJPMBW"),
    list("YXOWMSUKJQIETGBVLAZCNFRDHP"),
    list("LVRNXISBEWTPZCGUOKYHAJQMFD"),
    list("XGMDLUVHESWJCBAQKFZNTYPRIO"),
    list("DFOMEJHRLXNWVAKSTBIUPGZYQC"),
    list("RZJYWIGKHNTPEUSVLQOXFMDCBA"),
    list("TBEZJWUPGMDFSCVRQXIAKLNHOY"),
    list("HENZROYPGADUKXCWQFMVJBSTLI"),
    list("JPHDNZKTMYGORUCIFASLQWXEVB"),
    list("RJDNIEQSWBPZUOHMCVYXLAKGTF"),
    list("JULIOMZXBERTNHVFYGSACQWDPK"),
    list("GKTPISJCNVBMWXQFRYALHZEOUD"),
    list("QMUWJAPVCBHKDFGXTYLNIOEZSR"),
    list("HBOQCZRYIASWFLPUMNEKTJGXDV"),
    list("CWYLUQXPKAJSOHNBIEGDZVRTFM"),
    list("DZFMTLSAVYJGQBHXOCNRWUEIPK"),
    list("KRHQFLIGPSANOEWYCVZUMBDXTJ"),
    list("ZVMDIUJBGPRFXQNHYKOTASWCEL"),
    list("UMQJNRZXOHIWGFYCBDEVLKPATS"),
    list("NSMQYAOXHPCGKTZFLWVDBJRUEI"),
    list("OBQZGLEURAVWDKFHITXSNPMJYC"),
    list("BOTVYFUWACIQKLESZNHMPXGDRJ"),
    list("QTFCNDUMOLYHIPXWZSAJREGVBK"),
    list("FOJRGAUPXCVSNZYDETLBHIMQWK"),
    list("BCRVSMYNFGLQEDJTWZUPAKOXIH"),
    list("VFWAKTCQBLHXOYSZJEMPUNGDIR"),
    list("UFYENBGMPIRKHCXQAVWZJTLSDO"),
    list("VBMAFNYXTJLPKSHUOCGQZDEWIR"),
    list("HESNRLJABFWOGMUQXYKVIZDTCP"),
    list("EFWYPLUZMGHKJBQVRNXOITSADC"),
    list("AEGXKOIQWBPCZDLYRTJFSUVNHM"),
    list("YMBUWIGXSPRHCAFEOLZQNKTDVJ"),
    list("FZIMEHLTXSUDCAGVQPRWBJYONK")
]

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

text = "SENIG"

# Create a Figlet object with the desired font
figlet_font = pyfiglet.Figlet(font="standard")

# Render the text in ASCII art
ascii_art = figlet_font.renderText(text)

# Print the ASCII art

clear()
print(ascii_art)
print(Fore.RED + "Make by Bell")

while True:
    print(Fore.GREEN + "---------------------------------------------------")
    message = str(input("text:"))
    ss = input("en1 de2:")
    pin = input("PIN:")
    
    
    if int(ss) == 1:
        encoded_message = enigma_encode(message, rotors, alphabet)
        pinen= pin_enigma_encode(encoded_message, rotors, alphabet, pin)
        enm = encode_base64(pinen)
        print("Encoded message:", enm)
    elif int(ss) == 2:
        dem = decode_base64(message)
        message = pin_enigma_decode(dem, rotors, alphabet,pin)
        decoded_message = enigma_decode(message, rotors, alphabet)
        
        print("Decoded message:", decoded_message)

    else:
        print("ERROR")
