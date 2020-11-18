from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class emploitic:
    def __init__(self):
        self.browser = webdriver.Chrome('C:\\Users\\pc1\\Downloads\\chromedriver_win32\\chromedriver')
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
        print(a)
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
                print(str_)
                if(case == 0):
                    self.usd = str(str_)
                    print(self.usd)
                    self.curre.append(self.usd)
                    str_ = ""
                    case += 1
                else:
                    if(case == 1):
                        self.eur = str(str_)
                        print(self.eur)
                        self.curre.append(self.eur)
                        str_ = ""
                        case +=1
                    else:
                        if(case == 2):
                            self.gbp = str(str_)
                            print(self.gbp)
                            self.curre.append(self.gbp)
                            str_ = ""
                            case +=1
                        else:
                            self.jpy = str(str_)
                            print(self.jpy)
                            self.curre.append(self.jpy)
                            

    #def print_(self):


    def main(self):
        self.get_currencies()
        #self.print_()
        return self.curre
       



if __name__ == "__main__":
   
    a = emploitic()
    print(a.main())
    
   
    #element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.,"_eYtD2XCVieq6emjKBH3m")))
    
    
    
    

    
    
    #posts = element.find_elements_by_class_name("rpBJOHq2PR60pnwJlUyP0")
    #print(posts)
    #for post in posts:
            
    #elem = browser.find_elements_("result-list-style")
    #_eYtD2XCVieq6emjKBH3m
    #print(element.)
  
    #browser.quit()
    
    


'''
 headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    r = requests.get("https://www.emploitic.com/offres-d-emploi?t[0]=location-6&q=python",headers=headers)
    print(r.content)
    soup = bs(r.content,features="html.parser")
    p =  soup.find("div")
    print(p)
'''