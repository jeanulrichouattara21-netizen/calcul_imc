# def demander_nom():
#    reponse_nom=""
#    while reponse_nom=="":
#       reponse_nom=input("Quel est votre nom? ")
#    return reponse_nom

# def demander_age(nom_personne):
#    age=0
#    while age==0:
#       age_str=input(nom_personne + "  Quel est votre age? ")
#       try:
#          age=int(age_str)
#       except:
#          print("Erreur sur l'age entrer un age correcte")
#    return age

# def afficher(nom_pers,age_pers):
#    print()
#    print("Vous vous appeller " + nom_pers + " et vous avez " + str(age_pers) + " ans")
#    print("L'an prochain vous aurez " + str(age_pers+1) + " ans")
#    if age_pers==17:
#       print("Vous êtes presque majeur")
#    elif age_pers==18:
#       print("Vous êtes tout juste majeur: Felicitation")      
#    elif age_pers<10:
#       print("Vous êtes un enfant")
#    elif  12<=age_pers<18:
#       print("Vous êtes un adolescent")  
#    elif age_pers>60:
#       print("Vous êtes un senior")  
#    elif age_pers>=18:
#       print("Vous êtes un  majeur")    
#    else :
#       print("Vous êtes mineur")

      
# # NB_PERSONNES=3
# # for i in range(0,NB_PERSONNES):
# #    nom=demander_nom()
# #    age=demander_age(nom) 
# #    afficher(nom,age)


# def Acceuille():
#    nom_pers=demander_nom()
#    age_pers=demander_age(nom_pers)
#    afficher(nom_pers,age_pers)

# def information():
#     nom=input("Quel est votre nom?: ")
#     age=input("Quel est votre age?: ")

# def recuperer_info_personne(Numero_personne):
#     # information()
#     nom=input("Le nom de la personne" + str(Numero_personne) + ": ")
#     age=input("L'age de la personne"+ str(Numero_personne) +  ": ")
#     print("La personne",Numero_personne, "s'appelle" ,nom ," et à ",age ," ans ")
#     print("Le nom de la personne" ,Numero_personne , " comporte ",len(nom)," caractères")

# for i in range(0,3):
#     recuperer_info_personne(i+1)
#     print()

# def est_majeur(age):
#     if age <=0:
#       return False
#     if age>=18:
#         return True
#     else:
#         return False 

# def afficher_information(nom_pers,age=0):
#     if nom_pers=="":
#         print("Vous avez oublier le nom mais votre age est de " ,age , " ans")
#         return
#     if age==0:
#         print("Votre nom est " ,nom_pers )
#     else:
#         print(" Votre nom est " ,nom_pers , " et vous avez " ,age ," ans")

#     print("Votre nom comporte " ,len(nom_pers) , " caractères")
#     if est_majeur(age):
#         print("Vous êtes majeur")
#     else:
#         print("Vous êtes mineurs") 

# afficher_information("jean",20)         
# age=0
# majeur_ou_non=est_majeur(age)
# if majeur_ou_non:
#     print("Il est majeur")
# else:
#     print("Il es mineur")    


# def afficher_table_de_multiplication(n,min=0,max=10):
#     if min>max:
#         print("ERREUR:Le min est superieur au max")
#         return
#     for i in range(min,max+1):
#         print(i ,"x",n,"=",i*n)

# afficher_table_de_multiplication(4)    

def questionnaire():
    question=[
        {
            "question": "Quelle est la capitale de la France?",
            "choix":["a.Marseille", "b.Paris" ,"c.Nantes","d.Londres"],
            "reponse":"b"
        },
        { 
            "question": "Quelle est la couleur de l'orange?",
            "choix":["a.rouge", "b.orange" ,"c.noir","d.banane"],
            "reponse":"b"
        },
       
    ]

    for i,q in enumerate(question,start=1):
        print(f"{i}. {q['question']}")
        for option in q["choix"]:
            print(option)
        réponse = input("Votre choix : ").lower().strip()
        if réponse == q["reponse"]:
            print("Correct\n")
        else:
            print(f"Incorrect. La bonne réponse était : {q['réponse']}\n")
questionnaire()            