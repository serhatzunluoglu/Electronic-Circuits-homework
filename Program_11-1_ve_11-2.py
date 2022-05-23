# -*- coding: utf-8 -*-

# Serhat İsmail Zunluoğlu 20370031062

def fonksiyon1():
    # -------------------------------------------------------
    #               PROGRAM 11-1
    # -------------------------------------------------------
    #           KARMA PARAMETRELERİ KULLANARAK
    #               BJT AC ANALİZİ
    # -------------------------------------------------------

    print("""-------------------------------------------------------
                   PROGRAM 11-1
-------------------------------------------------------
            KARMA PARAMETRELERİ KULLANARAK
                BJT AC ANALİZİ
-------------------------------------------------------""")

    print("Bu program bir BJT devresinin AC analizini")
    print("Karma parametreleri kullanarak gerçekleştirir.")

    print("Aşağıdaki devre bilgilerini girin:")

    R1 = float(input("RB1="))
    R2 = float(input("RB2="))
    RC = float(input("RC="))

    RL = float(input("Yük direnci, RL="))
    RS = float(input("Kaynak direnci, RS="))
    VS = float(input("Kaynak gerilimi, VS="))
    print("BJT'nin karma parametresi değerlerini girin:")

    HI = float(input("hie="))
    HF = float(input("hfe="))
    HO = float(input("hoe="))
    HR = float(input("hre="))

    # -------------TANIMLAMA-------------
    RP = RC*RL/(RC+RL)
    RZ = HI-HF*HR*RP/(1+HO*RP)
    RB = R1*R2/(R1*R2)
    RI = RZ*RB/(RZ+RB)

    if(HO>0) and (HR>0):
        RT=1/(HO-HF*HR/(HI+RS))
    else:
        RT=1E+30

    RO=RT*RC/(RT+RC)
    AI=(RB/(RB+RZ))*(HF/(1+HO*RP))*(RC/(+RL))

    if (AI<.000001):
        AI=0
    AV=-HI*RC/(HI+(HI*HO-HF*HR)*RC)
    VI=RI*VS/(RI+RS)
    VO=AV*VI
    VL=VO*RL/(RO+RL)
    # -----------------------------------

    # REM BJT devresinin ac analizini yapar.

    print("AC analiz sonuçları:")

    print("Giriş empedansı, Ri=",RI/1000,"kiloohm")
    print("Çıkış empedansı, Ro=",RO/1000,"kiloohm")
    print("Gerilim kazancı(yüksüz), Av=",AV)
    print("Akım kazancı(IL/li), Ai=",AI)

    print("Çıkış gerilimi(yüksüz), Vo=",VO,"volt")
    print("Çıkış gerilimi(yük mevcut), VL=",VL,"volt")


    # REM Karma parametreleri kullanarak ac hesaplamalarını yapan modül

    RP=RC*RL/(RC+RL)
    RZ=HI-HF*HR*RP/(1+HO*RP)
    RB=R1*R2/(R1*R2)
    RI=RZ*RB/(RZ+RB)

    if(HO>0) and (HR>0):
        RT=1/(HO-HF*HR/(HI+RS))
    else:
        RT=1E+30

    RO=RT*RC/(RT+RC)
    AI=(RB/(RB+RZ))*(HF/(1+HO*RP))*(RC/(+RL))

    if (AI<.000001):
        AI=0
    AV=-HI*RC/(HI+(HI*HO-HF*HR)*RC)
    VI=RI*VS/(RI+RS)
    VO=AV*VI
    VL=VO*RL/(RO+RL)



def fonksiyon2():
    # -------------------------------------------------------
    #               PROGRAM 11-2
    # -------------------------------------------------------
    #           re ve BETA PARAMETRELERİNİ KULLANARAK
    #                   BJT'NİN AC ANALİZİ

    print("""-------------------------------------------------------
                   PROGRAM 11-2
-------------------------------------------------------
            re ve BETA PARAMETRELERİNİ KULLANARAK
                    BJT'NİN AC ANALİZİ""")

    print("Bu program re ve beta parametrelerini kullanarak")
    print("bir BJT'nin ac analizini gerçekleştirir.")


    print("Aşağıdaki devre bilgilerini girin:")

    R1 = float(input("RB1="))
    R2 = float(input("RB2="))
    RC = float(input("RC="))
    E1 = float(input("KÖPRÜLENMİŞ EMETÖR DİRENCİ,RE1="))
    E2 = float(input("KÖPRÜLENEN EMETÖR DİRENCİ,RE2="))


    BETA = float(input("Beta="))
    CC = float(input("Besleme Gerilimi, VCC="))
    RL = float(input("Yük direnci, RL="))
    RS = float(input("Kaynak direnci, RS="))
    VS = float(input("Kaynak Gerilimi, VS="))

    # REM re modelini kullanarak BJT ac analizi yapan modül
    RB = R1 * (R2 / (R1 + R2))
    DE = RC*(RL/(RC+RL))
    BB = R2 * (CC / (R1 + R2))
    IE = (BB - .7) * (BETA + 1) / (RB + BETA * (E1 + E2))
    RE = .026 / IE
    R3 = BETA * (RE + E1)
    RI = RB * (R3 / (RB + R3))
    RO = RC
    AI = (RC / (RC + RL)) * BETA * (RB / (RB + R3))
    AV = -RC / (E1 + RE)
    VI = VS * (RI / (RI + RS))
    VO = AV * VI
    VL = VO * (RL / (RO + RL))

    HI = float(input("hie="))
    HF = float(input("hfe="))
    HO = float(input("hoe="))
    HR = float(input("hre="))



    #REM ac analizi gerçekleştirir
    print("AC analizi sonuçları:")
    print("Transistörün dinamik direnci, re=",RE,"ohm")

    if CC-IE*(RC+E1+E2)<=0:
        print("Devre Doymada")


    print("Giriş empedansı,Ri=",RI,"ohm")
    print("Çıkış empedansı,Ro=",RO,"ohm")
    print("Gerilim kazancı(yüksüz),Av=",AV)
    print("Akım kazancı, Aİ=",AI)

    print("Çıkış gerilimi(yüksüz),Vo=",VO,"volt")
    print("Çıkış gerilimi(yük-altında),VL=",VL,"volt")

    VM=CC-IE*(BETA/BETA+1)*(RC+E1+E2) # REM Maximum sinyal sapması

    if VL>VM:
        print("Maximum distorsiyonsuz çıkış",VM,"volt")

    # REM re modelini kullanarak BJT ac analizi yapan modül
    RB = R1*(R2/(R1+R2))
    RP = RC*(RL/(RC+RL))
    BB = R2*CC/(R1+R2)
    IE = (BB-.7)*(BETA+1)/(RB+BETA*(E1+E2))
    RE = .026/IE
    R3 = BETA*(RE+E1)
    RI = RB*(R3/(RB+R3))
    RO = RC
    AI = (RC/(RC+RL))*BETA*(RB/(RB+R3))
    AV = -RC/(E1+RE)
    VI = VS*(RI/(RI+RS))
    VO = AV*VI
    VL = VO*(RL/(RO+RL))


while True:
    # ------------Program seçiminin olduğu kısım------------
    print("1-) Program 11-1")
    print("2-) Program 11-2")
    choice=input("Lütfen kullanmak istediğiniz programı seçiniz=")

    if choice == "1":
        fonksiyon1()
    elif choice == "2":
        fonksiyon2()
    else:
        print("Hatalı seçim lütfen tekrar seçim yapınız !")


