








def main():

    casos = int(input())

    for _ in range(casos):

        temp = input().split(" ")

        nDocumentos = int(temp[0])
        mDependencias = int(temp[1])

        print(f"sao {nDocumentos} documentos e {mDependencias} dependencias")
        for i in range(mDependencias):

            temp = input().split(" ")
            
            depende = int(temp[0])
            documento = int(temp[1])
            print(f"o doc {depende} depende do documento {documento}")

        print("-------------------")






    return 0


if __name__ == "__main__":
    main()