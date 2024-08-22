import os, shutil
import time

#implement '.env' (hide important variables/informations)
absolute_path="G:/Meu Drive/0curent_work_folder/work_sincronizado_driver/dev/engenharia"

#Create a directory
os.mkdir("dinamyc_files")
#Change to the new directory
os.chdir("dinamyc_files")

#Create dile and writr to it
with open("created_file.py", "w") as file:
    file.write("Test = 'Test'")
    file.close()
    #Verify the file and its content
    print(10*"=", os.listdir())
    print(10*"=", os.path.isfile("/created_file.py"))
    print(10*"=", os.path.isdir("/dinamyc_files"))
    resposta = input("Caso va rodar o codigo novamente digite 'S', para nao ter problemas as pastas dinamicas: ")

    if resposta.upper() == 'S':
        os.remove("created_file.py")
        time.sleep(2)
        print(f"{absolute_path}+pytho_domain_expansion")
        os.chdir(f"{absolute_path}/pytho_domain_expansion")
        os.rmdir("dinamyc_files") # empty-dir
        # shutil.rmtre("nonempty-dir")