import os

with open("oneclick_toolkit/national_focus_shine.txt","r") as file1:
    shinecontent_raw = file1.read()

with open("national_focus.gfx","w") as file2:
    file2.write('spriteTypes = {\n')

for filename in os.listdir(os.getcwd()):
    if '.' in filename:
        if not('.py' in  filename) and not('.gfx' in  filename):
            filename_noextension = '.'.join(filename.split('.',1)[:-1])
            shinecontent = shinecontent_raw.replace('*m*a*s*k*',filename)
            with open("national_focus.gfx","a") as file2:
                file2.write('\tSpriteType = {\n\t\tname = \"GFX_'+filename_noextension+'_shine\"\n\t\ttexturefile = \"*PATH_TO_REPLACE*'+filename+'\"'+shinecontent+'\n\t}\n')

with open("national_focus.gfx","a") as file2:
    file2.write('}')