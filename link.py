print("These are the links to the websites.")
#have:Google Facebook Instagram Youtube G-mail 
#       1       2         3        4       5  
#Tinkercad Github Scratch
#    6       7      8
#not have:Google-Drive microbit
print("\n1:Google   2:Facebook   3:Instagram   \n\n4:Youtube   5:G-mail   6:Tinkercad   \n\n7:Github   8:Scratch (Blocks for kid)   ")
ll=int(input("\nEnter the number of the website you want.(Only One!)\n"))
if ll==1:
    print("Google:\nhttps://www.google.com/")
elif ll==2:
    print("Facebook:\nhttps://www.facebook.com/")
elif ll==3:
    print("Instagram:\nhttps://www.instagram.com/?hl=zh-tw")
elif ll==4:
    print("Youtube:\nhttps://www.youtube.com/")
#have:Google Facebook Instagram Youtube G-mail 
#       1       2         3        4       5  
#Tinkercad Github Scratch
#    6       7      8
#not have:Google-Drive microbit
elif ll==5:
    print("G-mail:\nhttps://www.google.com/gmail/about/")
elif ll==6:
    print("tinkercad:\nhttps://www.tinkercad.com/")
elif ll==7:
    print("Github:\nhttps://circleci.com/integrations/github/?utm_source=gnb&utm_medium=SEM&utm_campaign=SEM-gnb-Github-Eng-ni&utm_content=SEM-gnb-Github-Eng-ni-Github&gclid=EAIaIQobChMI0_i8nrS55wIVCkHTCh3r8gBOEAAYASAAEgLzxfD_BwE")
elif ll==8:
    print("Scratch (Blocks for kid):\nhttps://scratch.mit.edu/")
else:
    print("We haven't set the website you want.")