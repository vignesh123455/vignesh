import os
import shutil

#print(os.environ.get('path'))
#print(os.environ["TMP"])
#path = os.chdir(r"C:\Users\VGS2COB\Practice\Project")
path = os.getcwd()
source = r"C:\Users\VGS2COB\Practice\projects"
destination = r"C:\Users\VGS2COB\Practice\vignesh"
#print(os.getlogin())
#print(os.getppid())
#print(os.listdir(path))

lst1=[]

dict1 = {
    
    'Wssrl_line'            : 'CSWBasicTest93_WssFailure_003',
    'Wssrr_line'            : 'CSWBasicTest93_WssFailure_004',
    'EBDKA'                 : 'CSWBasicTest93_LampCheck_002',
    'ECE13_Error'           : 'CSWBasicTest93_LampCheck_003',
    'Wssfl_line'            : 'CSWBasicTest93_WssFailure_001',
    'Wssfr_line'            : 'CSWBasicTest93_WssFailure_002',
    'BoschDiag'             : 'CSWBasicTest93_BoschDiagnosis_001',
    'CustDiag'              : 'CSWBasicTest93_CustomerDiagnosis_001',
    'ABSKA'                 : 'CSWBasicTest93_LampCheck_004',
    'ABS'                   : 'CSWBasicTest93_RuntimeChecks_001',
    'TCS'                   : 'CSWBasicTest93_RuntimeChecks_002',
    'Double_Lane_Change'    : 'CSWBasicTest93_RuntimeChecks_003',
    'System_States_01'      : 'CSWBasicTest93_SystemStates_001',
    'EV_Gnd'                : 'CSWBasicTest93_ValveChecks_001',
    'EV_AV'                 : 'CSWBasicTest93_ValveChecks_002',
    
    }


for roots,dirs,files in os.walk(source):
    for file in files:
       # print(file.endswith('html')) 
        if file.endswith('.html'):
            for y in dict1.keys():
                x = y
                #print("the value of x is ", x)
                res = [i for i in files if x in i]
                if res not in lst1:
                   # print("The res is ", res)
                    source_file = source + '\\' + str(res[0])
                    destination_file = destination + '\\' + str(res[0])
                  #  print("The source file is :",source_file)
                  #  print("The destination file is :",destination_file)
                    #a = os.path.isfile(str(res))
                    #print("THe value of a is ", a)
                    if str(res[0]) not in lst1:
                        if os.path.isfile(source_file):
                            shutil.copyfile(source_file,destination_file)
                           # print('Copied :',file)
                          #  print("the res of dict is ", dict1[res[0]])
                            z = destination + '\\' + dict1[x] + str('.html')                          
                         #   print("the value of z is ", z)
                            os.rename(destination_file,z)
                            lst1.append(str(res))
                            print("The lst1 container : ",str(res))   
                            
            break
                              
                                                 
                            