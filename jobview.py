from zoautil_py import jobs

JOBID = str(input("JOBID que deseja visualizar:"))
dictjob = jobs.list_dds(JOBID)
for i in dictjob:
    print("stepname:"+i.get("stepname")+" dataset:"+i.get("dataset"))

entrada = str(input("Qual DS deseja ler?(stepname + dataset):"))

ddvals = entrada.split(" ")
ddcont = jobs.read_output(JOBID,ddvals[0] , ddvals[1])

entrada = input("console ou arquivo?:")
if(entrada == "console"):
    print(ddcont)
elif(entrada == "arquivo"):
    entrada = input("caminho e nome do arquivo onde deseja salvar:")
    arq = open(entrada,"a")
    arq.write(ddcont)
    arq.close()
else:
    print("Valor invalido,imprimindo em console")

