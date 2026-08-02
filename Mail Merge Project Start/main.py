#TODO: Create a letter using starting_letter.txt

with open("./input/Letters/starting_letter.txt") as file:
        st_ltr = file.read()
        print(st_ltr)

with open("./input/Names/invited_names.txt") as file_1:
        in_ltr = file_1.readlines()
        print(in_ltr)

        for names in in_ltr:
                stripped_name = names.strip()
                new_letter = st_ltr.replace("[name]",stripped_name)
                with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as output:
                        output.write(new_letter)





#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp