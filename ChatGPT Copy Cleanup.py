

def chatgptcleanup(input_char):

    gpt_cleanup = ""

    for symbol in input_char:
        if symbol != '*' and symbol != "#":
            gpt_cleanup += symbol
             
    return gpt_cleanup
         

#Insert Prompt Here

copy_gpt = '''

   insert text data here _ Mon**aj#jk*kjsd## _ run to test

'''

updated_cleanup = chatgptcleanup(copy_gpt)

print (updated_cleanup)
