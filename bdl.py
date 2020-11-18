from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class bdl:
    def __init__(self,webd):
        self.browser = webdriver.Chrome(webd)
        self.browser.get('https://www.bdl.dz/Algerie/index1.htm')
        self.usd = ""
        self.eur = ""
        self.gbp = ""
        self.jpy = ""
        self.curre = []

    def get_currencies(self):
        elem = self.browser.find_element_by_tag_name("p")
        string = "Avis aux opérateurs économiques   |     Avis d'appel d'offre    |     Conditions de Banque    |     "
        string2 = "Cours de principales monnaies: "
        a = elem.text.replace(string,'')
        a = a.replace(string2, '')
        #print(a)
        self.format_(a)
    
    def format_(self, a):
        a = a+"-"
        str_ = ""
        j = 1
        case = 0
        for i in a:
            if(i != "-" and a.index(i) != len(a) - 1):
                if(i == " "):
                    if(j == 3):
                        j = j + 1
                        continue #Not including the space
                    else : 
                        if (j == 4):
                            j = 1
                            continue
                        else: 
                            j +=1

                str_ += i
                
            else:
                if(case == 0):
                    self.usd = str(str_)
                    #print(self.usd)
                    self.curre.append(self.usd)
                    str_ = ""
                    case += 1
                else:
                    if(case == 1):
                        self.eur = str(str_)
                        #print(self.eur)
                        self.curre.append(self.eur)
                        str_ = ""
                        case +=1
                    else:
                        if(case == 2):
                            self.gbp = str(str_)
                            #print(self.gbp)
                            self.curre.append(self.gbp)
                            str_ = ""
                            case +=1
                        else:
                            self.jpy = str(str_)
                            #print(self.jpy)
                            self.curre.append(self.jpy)
                            

    #def print_(self):


    def main(self):
        self.get_currencies()
        #self.print_()
        return self.curre
       

'''
#EXEMPLE

if __name__ == "__main__":
    username = "machine" #your username here or you can directly put the path in webdriver_
    webdriver_ = f'C:\\Users\\{username}\\Downloads\\chromedriver_win32\\chromedriver'.format(username) 
    a = bdl(webdriver_)
    print(a.main())

'''
